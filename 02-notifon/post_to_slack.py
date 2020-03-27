# coding: utf-8
import requests
url = 'https://hooks.slack.com/services/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' 
data = { "text": "Hello, world." }
requests.post(url, json=data)
