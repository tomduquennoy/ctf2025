import math
import requests

data = {"number": "161",
        "answer": "(2, 3)",
        "user": "t.duquennoy"}
r = requests.post("http://34.163.196.38/", data=data)
print(r.text)


