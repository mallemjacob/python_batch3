import requests, pprint

# response = requests.get('https://jsonplaceholder.typicode.com/todos/')

weatherapi = 'https://api.open-meteo.com/v1/forecast?latitude=16.3067&longitude=80.4365&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'


response = requests.get(weatherapi)

# convert json data into dictionary
output = response.json()

# pprint.pprint(output[-1]['title'])
# print(len(output))
pprint.pprint(output)