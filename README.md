REST service for storing binary data in the S3 cloud service
# Installations
+ Clone the repository

 ```
 git clone git@github.com:hrumarko/binarycloud.git
 ```
 
+ Set up a virtual environment

 ```
 python3 -m venv venv
 ```
 
 ```
 source venv/bin/activate
 ```
 
+ Set up the dependencies

 ```
 pip install -r requirements.txt
 ```
 
+ Configure the configuration for S3

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration

+ Change `BUCKET` to the name of your bucket and `FILE` to the name of the file where the data will be saved.

+ Launch of service
 ```
 uvicorn main:app --reload
 ```


# Using

 Creating/adding data
 ```
http://127.0.0.1:8000/api/v1//create-data/?key=<KEY>&value=<VALUE>
```
  Getting data
```
http://127.0.0.1:8000/api/v1/get-data/<key>
```
  Documentation
```
http://127.0.0.1:8000/docs
```
