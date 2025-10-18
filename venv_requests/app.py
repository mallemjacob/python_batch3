import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/')

output = response.json()

print(output)