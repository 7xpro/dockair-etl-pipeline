import requests
import os 
import pandas as pd

def get_data():
    

    url ='https://687f4437efe65e52008902d3.mockapi.io/testapi/products'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        df=pd.DataFrame(data)
        df['price'] = df['price'].astype(float)
        df['id'] = df['id'].astype(int)
        
        df.to_json('/opt/airflow/data/products.json',orient="records",lines=True)
        print('upladed succesfully')
        
    else:
        print(f"Error: {response.status_code}")
        print("Failed to retrieve data.")    
get_data()

    
    