# coding: utf-8
import boto3
session = boto3.Session()
s3 = session.resource('s3')
bucket = s3.create_bucket(
                Bucket='mouadvideolyzervideos', 
                                CreateBucketConfiguration={'LocationConstraint': 'us-east-2'}
                                            )
from pathlib import path
from pathlib import Path
get_ipython().run_line_magic('ls', '/home/ec2-user/environment/automating-aws-with-python/03-videolyzer/*.mp4')
pathname = '~/environment/automating-aws-with-python/03-videolyzer/563399566.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition-client  = session.client('rekognition')
rekognition_client  = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
rekognition_client  = session.client('rekognition', region_name='us-east-2')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
response
job_id = se['JobId']
job_id = response['JobId']
job_id
result = rekognition_client.get_label_detection(JobId=job_id)
result
result['JobStatus']
