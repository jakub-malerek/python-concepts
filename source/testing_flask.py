import requests
import json

# r = requests.get("http://127.0.0.1:5000/stores")

# print(r.json())

# print("-------------------------------------------")

# r = requests.post("http://127.0.0.1:5000/stores", json={"name":"najki"})

# print(r.json())

# print("-------------------------------------------")

r = requests.get("http://127.0.0.1:5000/stores")

print(json.dumps(r.json()))





