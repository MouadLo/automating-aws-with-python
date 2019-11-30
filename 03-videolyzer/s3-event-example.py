# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2019-11-30T06:38:33.814Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AROA5SES46RLWARX53EL5:i-04ccbb61d2454973f'}, 'requestParameters': {'sourceIPAddress': '3.16.136.25'}, 'responseElements': {'x-amz-request-id': 'A4397DAD14BCA867', 'x-amz-id-2': 'k6w7KQYU2eVA8xcGfJHJVe0ZpvdjuxoUG6Js0lMXJxg962psWaTH8aaXvYXC5Akk4tafRbeDSw0='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '86ad8099-ecbd-416e-9d9d-6ce31d4ff554', 'bucket': {'name': 'mouadvideolyzervideosxfgfd', 'ownerIdentity': {'principalId': 'A3GGMIH2VQV7SO'}, 'arn': 'arn:aws:s3:::mouadvideolyzervideosxfgfd'}, 'object': {'key': '1401996156.mp4', 'size': 2660865, 'eTag': 'a24b1ee961c664cea84baaf6d8be3b9e', 'sequencer': '005DE20E698804F4E9'}}}]}
event
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
