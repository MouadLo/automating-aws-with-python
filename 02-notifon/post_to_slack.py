# coding: utf-8
import requests
url = '' # Replace with slack webhook URL
data = { "text": "Hello, from python boto3" }
requests.post(url, json=data)
