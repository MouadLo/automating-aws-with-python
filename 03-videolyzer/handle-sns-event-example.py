# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:932315984983:handleLabelDetectionTopic:4a10fd2b-46a7-4742-a6e0-4e660a1c688c', 'Sns': {'Type': 'Notification', 'MessageId': '5cca9aff-e351-52cb-8330-cca3c0b3d730', 'TopicArn': 'arn:aws:sns:us-east-1:932315984983:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"cefc855ecd77f28d877e8c6b916aa546b9b3fda0e2e1f43afa145df7246bada6","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1575100834265,"Video":{"S3ObjectName":"Blurry Video Of People Working.mp4","S3Bucket":"mouadvideolyzervideosxfgfd"}}', 'Timestamp': '2019-11-30T08:00:34.298Z', 'SignatureVersion': '1', 'Signature': 'gqjOn9wMUhqmLwAzXGoGWE379OGx6fE/lSEhX+EYKQfrYO0FMgGjqrVaLu8nIWL9DLeoRqyg6i462e3q0gAcJXslnJCxNTCe5h3dqUvVaygK372vpiKBIjHNDNFyOwN1FuDHPPTk3neq8NpaXfnFNRCPI6+woskcCrWUWae+rLxHF7PuuFrwAcoEoaLEtmpmx+YgzPY2XhcMS5lyY3aCgk8rKwzpvAIrTslBriH8BDQV0eb9ny9b4Pu7nZjSz1Z2A9TRygyZlilH8Pu4cl02+DIcoZ8kbfJlbHjuI8ze3t3brdUoRyLCbedtbLs6JOo4UifESDJW4+SLfVnNVHEAZQ==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:932315984983:handleLabelDetectionTopic:4a10fd2b-46a7-4742-a6e0-4e660a1c688c', 'MessageAttributes': {}}}]}
event.keys()
event['Records'][0].keys()
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['Sns']
event['Records'][0]['Sns']['Message']
event['Records'][0]['Sns']['Message']['JobId']
import json
json.loads(event['Records'][0]['Sns']['Message'])
