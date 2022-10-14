import requests as req
import json, time

url = 'http://localhost:8080/remove'
param = {'id': '01', 'n': 'virtual device', 'k': '5289'}
response = req.post(url, data = param)

print(response.text)