import math
import requests

data = {"number": "193",
        "answer": "(63,47,24)",
        "user": "t.duquennoy"}
r = requests.post("http://34.163.196.38/", data=data)
print(r.text)





