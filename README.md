# 🛠️ Dockerized ETL Pipeline with Airflow, AWS, and Athena

This project demonstrates a complete ETL pipeline using Docker and Apache Airflow to orchestrate tasks that fetch data from a public API, store it locally, upload it to AWS S3, trigger a Glue Crawler to update schema, and query the data using AWS Athena.


📌 Key Features

- Built using Docker and Apache Airflow
- Fetches data from a **MockAPI**
- Stores data locally for historical tracking
- Uploads data to **AWS S3** partitioned by `year/month.day`
- Automatically triggers **AWS Glue Crawler** to infer schema
- Runs SQL queries using **AWS Athena**
- Modular Python scripts for each ETL step

---

🔧 Project Architecture

<img width="931" height="421" alt="newdir drawio" src="https://github.com/user-attachments/assets/e2b02147-2d40-475c-837e-2f76527b69c0" />


📂 Project Structure
---
    ├── dags/ 
    │   ├── etl_dag.py          # Main Airflow DAG to orchestrate all tasks
    │   ├── source.py           # Fetches data from MockAPI and saves locally
    │   ├── localtos3.py        # Uploads local file to AWS S3
    │   ├── runcrawler.py       # Triggers AWS Glue Crawler
    │   └── runathena.py        # Runs Athena SQL queries
    ├── docker-compose.yml      # Docker Compose setup for Airflow
    ├── .env                    # AWS credentials and env configs
    ├── README.md
    |-- data/
        |--products.json


🚀 Getting Started

  - Prerequisites:
    - Docker
    - AWS credentials with access to:
      - S3
      - Glue
      - Athena
     
        
1 - Setup Instructions:

    - clone this repository:
    
           - git clone https://github.com/7xpro/dockair-etl-pipeline.git
           - cd dockair-etl-pipeline
    
     
2 - Add your credentials in a .env file
  --

     - BUCKET_NAME=s3bucket_name
     - FILE_KEY=key_to_file.json
     - CRAWLER_NAME= crawler_name
     - REGION_NAME=ap-south-1 # region for AWS services
     - DATABASE_NAME=database_name # name of the database for crawler
     - OUTPUT_BUCKET=s3://outbucket_for_athena_query_results
     - TABLE_NAME=table_name_created_by_crawler
     - AWS_ACCESS_KEY_ID=aw_access_key_id
     - AWS_SECRET_ACCESS_KEY=aws_secret_access_key
     - AWS_DEFAULT_REGION=ap-south-1 #region for AWS services
      
      #replace the above values with your actual AWS credentials and configurations

   
3 - Start the Airflow environment:
<br>
  - 
      docker-compose up --build  
<br>
4 - Open Airflow UI at http://localhost:8080<br>
5 - Trigger the etl_dag from the Airflow dashboard.<br>

<br>
🧪 Technologies Used:

    - Docker<br>
    - Airflow<br>
    - AWS S3<br>
    - AWS Glue<br>
    - AWS Athena<br>
    - Python<br>
    - Boto3<br>

🎥 Demo<br>

     


    





