import boto3
import json
from fastapi import FastAPI

app = FastAPI()
s3 = boto3.client('s3')

FILE = 'binarydata.txt'
BUCKET = 'marinovbucket'

    
@app.put("/api/v1//create-data/", status_code=201)
def put_data(key, value):
    """Creating data on the cloud with a key and a value"""
    data_json = get_json_from_s3()
    if data_json is None:
        return {'Error': 'Check your data(FILE, BUCKET, credentials)'}
    else:
        data_json[key] = value
        data = json.dumps(data_json)
        s3.put_object(Body=data, Bucket=BUCKET, Key=FILE)
        return { 'Succes': 'You posted'}
    

@app.get("/api/v1/get-data/{key}")
def get_data(key):
    """Retrieving data from the cloud with a key"""
    data = get_json_from_s3()
    if data is None:
        return {'Error': 'Check your data(FILE, BUCKET, credentials)'}
    elif key not in data.keys():
        return {'Error': 'Non-existent key'}
    else:
        return { key: data[key]}


def get_json_from_s3():
    """Retrieving a file from the cloud and converting it to a JSON or return an empty dictionary if the file is missing """
    try:
        try:
            obj = s3.get_object(Bucket=BUCKET, Key=FILE)
            data = obj['Body'].read()
            return json.loads(data.decode(encoding='utf-8'))
        except:
            return {}
    except:
        return None

