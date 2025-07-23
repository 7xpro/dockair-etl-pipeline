from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta
from source import get_data
from runathena import athena
from runcrawler import crawler
from localtos3 import s3upload

default_args={
    'start_date':datetime(2025,7,22),
    'retries':1,
    
}


with DAG(
    
    dag_id="elt_dockair-dag",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['api','etl']
    
)as dag:
    get_task=PythonOperator(
        task_id='get_data',
        python_callable=get_data
        
    )
    
    s3=PythonOperator(
        task_id="s3_upload",
        python_callable=s3upload
    )

    crawl=PythonOperator(
        task_id="crawler",
        python_callable=crawler
    )
    
    athen=PythonOperator(
        task_id="athena",
        python_callable=athena,
        retries=2,
        retry_delay=timedelta(minutes=1)
    )
    
    get_task>>s3>>crawl>>athen
    # athen