# coding: utf-8
import boto3
session = boto3.session.Session()
s3 = session.resource('s3')

    

# Create a bucket in the S3 default region (us-east-2)
#new_bucket = s3.create_bucket(Bucket='automatinh-aws-boto3-python-s3', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

#for bucket in s3.buckets.all():
#    print(bucket)



from pprint import pprint

paginator = s3.meta.client.get_paginator('list_objects_v2')
for page in paginator.paginate(Bucket='automating-static-website'):
    for obj in page.get('Contents', []):
        pprint(obj)

