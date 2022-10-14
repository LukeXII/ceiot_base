import requests as req
import json, time

lat = '-34.6'
lon = '-58.45'
api_key = '9cd14d5a1501937456dc34672558bcda'

url = 'http://localhost:8080/device'
param = {'id': '02', 'n': 'virtual device', 'k': '5289'}
response = req.post(url, data = param)

print(response.text)

while True:
    response = req.get('https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + api_key)

    # print(response.text)
    # print(type(response.text))

    data = json.loads(response.text)

    # print(data)
    # print(type(data))

    temp_city = data['main']['temp'] - 273
    pressure_city = data['main']['pressure']

    url = 'http://localhost:8080/measurement'
    param = {'t': round(temp_city, 1), 'p': pressure_city, 'id': 'virtual device'}

    response = req.post(url, data = param)

    print(response.text)

    time.sleep(5)