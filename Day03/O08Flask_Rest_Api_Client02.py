
import json

import requests

print("get".center(60, "-"))

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getproduct/Pepsi")

res = response.json()

# print(res)
for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
