import boto3
import os 
from dotenv import load_dotenv
import time


def athena():
    
    load_dotenv('/opt/airflow/.env')
    # load_dotenv()
    athena=boto3.client('athena')

    database=os.getenv('DATABASE_NAME')
    table=os.getenv('TABLE_NAME')
    output_location=os.getenv('OUTPUT_BUCKET')
    print(database, table, output_location  )

    query=f"""

    SELECT * FROM {table} WHERE price>300

    """
    try:
        response=athena.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database':database
            },
            ResultConfiguration={
                'OutputLocation':output_location
            }  
        )
        
        query_execution_id=response['QueryExecutionId']
        print(f"Started Query with Execution id: {query_execution_id}")
        
        while True:
            result=athena.get_query_execution(QueryExecutionId=query_execution_id)
            state=result['QueryExecution']['Status']['State']
            if state in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
                print(f"Query execution state: {state}")
                break
            print("Waitin for query to complete...")
            time.sleep(2)
            
        if state == 'SUCCEEDED':
            print("Query executed successfully.")
                
        
    except Exception as e:
        print(f"failed to execute the query error: {e}")
        
  