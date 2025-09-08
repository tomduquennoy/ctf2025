import math
import requests

data = {"number": "180",
        "answer": "argmax",
        "user": "t.duquennoy"}
r = requests.post("http://34.163.196.38/", data=data)
print(r.text)





