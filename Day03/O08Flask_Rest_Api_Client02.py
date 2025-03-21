
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

print("put".center(60, "-"))
response = requests.put(BASE + 'getproduct/Coke', data={'cat': 'baverage'})

res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("patch".center(60, "-"))
data = {'price': 5000}
response = requests.patch(BASE + 'getproduct/Pepsi', json=json.dumps(data))

res= response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("post".center(60, "-"))
fanta = {'item': '100ml Bottle', 'price': 20, 'qty': 285}

response = requests.post(BASE + "getproduct/fanta", json=json.dumps(fanta))
res = response.json()

for ky, info in res.items():
    print(str(ky).upper())
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("Delete".center(60, "-"))
response = requests.delete(BASE + "getproduct/Thumbs_up")
res = response.json()


for ky, info in res.items():
    print(str(ky).upper())
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)
