# my own module  =  m1
# buildin module = random
# 3rd pary module = requests

import m1, random, requests
print('Hello welcome')

print(m1.greet())

r = requests.get('https://jsonplaceholder.typicode.com/todos/1')

o = r.json()

print(o)