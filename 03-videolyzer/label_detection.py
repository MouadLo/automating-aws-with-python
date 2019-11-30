# coding: utf-8
import boto3
from pathlib import Path

session = boto3.Session()
s3 = session.resource('s3')

#bucket = s3.create_bucket(Bucket='mouadvideolyzervideos', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
         

pathname = '~/environment/automating-aws-with-python/03-videolyzer/563399566.mp4'

path = Path(pathname).expanduser().resolve()

print(path)

#bucket.upload_file(str(path), str(path.name))


rekognition_client  = session.client('rekognition', region_name='us-east-2')
#response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': 'mouadvideolyzervideos', 'Name': path.name}})
#print(response)

#job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId='867f18ff6fe51f2e1ef5c5ba00ae3751df939885da45a339abd16168f013b333')

print(result)

print(result['JobStatus'])


# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='robinvideolyzervideos')
bucket = s3.create_bucket(Bucket='robinvideolyzervideos', LocationConstraint=session.region_name)
bucket = s3.create_bucket(Bucket='robinvideolyzervideos')
bucket = s3.create_bucket(Bucket='robinvideolyzervideos', CreateBucketConfiguration={'LocationConstraint': session.region_name})
from pathlib import Path

pathname = '~/environment/automating-aws-with-python/03-videolyzer/563399566.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client  = session.client('rekognition', region_name='us-east-2')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']
result['Labels']
len(result['Labels'])