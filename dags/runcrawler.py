import boto3
import os 
from dotenv import load_dotenv
import time


def crawler():
    
    load_dotenv('/opt/airflow/.env')

    crawler_name=os.getenv('CRAWLER_NAME')
    region = os.getenv('AWS_REGION','ap-south-1')
    if crawler_name !=""  and region!="":
        glue = boto3.client('glue',region_name=region)
        
    response=glue.start_crawler(Name=crawler_name)

    print(f"Crawler {crawler_name} started.")     
    while True:
        response = glue.get_crawler(Name=crawler_name)
        state = response['Crawler']['State']
        if state in ['READY', 'STOPPING', 'STOPPED']:
            print(f"Crawler state: {state}")
            break
        print("Waiting for crawler to complete...")
        time.sleep(10)