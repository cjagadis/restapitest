import requests
import json

d = open("data.json", "r").read()

r = requests.post("https://reqres.in/api/users", data=json.loads(d))
print(r)
print(r.json())
assert r.json()['job']=='emperor'

print(r.headers.get("Content-Type"))
