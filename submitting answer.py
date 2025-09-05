import requests

data = {"number": "65",
        "answer": "https://github.com/SupaeroDataScience/machine-learning.git",
        "user": "a.barberin"}
r = requests.post("http://34.163.196.38/", data=data)
print(r.text)
