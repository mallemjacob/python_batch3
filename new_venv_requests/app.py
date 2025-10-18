import requests
from flask import Flask

print('Enter an id number:')
user_input = input()

response = requests.get('https://jsonplaceholder.typicode.com/todos/' + user_input)

output = response.json()

fn = output['title']


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>" + fn + "</p>"