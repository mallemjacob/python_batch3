import requests
import webbrowser


# names = []

# gh_link = 'https://api.github.com/search/repositories?q=language:python+sort:stars'

# response = requests.get(gh_link)

# #convert the JSON response into python object

# output = response.json()

# # print(output["items"][0]["name"])

# # print(output["items"])

# for item in output["items"]:
#     # print(item["name"])
#     if not item["private"]:
#         names = names + [item["name"]]

# print(names)

# spam = ['cat','bat','dog']

# for i in spam:
#     print(i)

# dict = { "name" : "a1", "colors": [{"n":"a"},{},{}] }
# print(dict["colors"][0]["n"])



# print("Enter a keyword to search: ")
# query = input()

unspash_api = "https://api.unsplash.com/photos/?client_id=PDZH_6EZMr9nJxiyr2I8VmBHpuErI0WF0VTOgJtysLg"

response = requests.get(unspash_api)

output = response.json()

print(output[0]["alt_description"])

# url = output[0]["urls"]["regular"]

url = "https://images.unsplash.com/photo-1761872936204-07e2bbe1990b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2Mzk2NDN8MHwxfGFsbHwzfHx8fHx8fHwxNzYyMTY2Mzk0fA&ixlib=rb-4.1.0&q=80&w=400"

# webbrowser.open(url)


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<img src="+url+" height=400 width=400/>"