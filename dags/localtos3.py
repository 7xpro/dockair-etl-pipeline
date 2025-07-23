import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

def s3upload():
    

    path=datetime.now().strftime('year=%Y/month=%m/day=%d/')

    load_dotenv('/opt/airflow/.env')

    s3 =boto3.client('s3')
    try:
        bucket_name=os.getenv('BUCKET_NAME')
        key=os.getenv('FILE_KEY')
        
        full_path=os.path.join("input/",path,key)
        
        try:
            s3.upload_file('/opt/airflow/data/products.json',bucket_name,full_path)
            print(f"uploaded")
        
        except Exception as e:
        
            print(f"Error uploading file to S3: {e}")   
        
    except Exception as e:
        print(f"Error loading environment variables: {e}")
    
