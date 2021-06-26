import requests
import json

r = requests.delete("https://reqres.in/api/users/2")
print(r)
assert r.status_code==204, "User deletion failed"