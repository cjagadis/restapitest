# testing Post

import requests

payload = {
    "name": "morpheus",
    "job": "leader"
}

pload = {
    "name": "foo",
    "job": "emperor"
}

p = requests.post('https://reqres.in/api/users', data=payload)

print(p)
print(p.json())

p = requests.post('https://reqres.in/api/users', data=pload)

print(p)
print(p.json())
assert p.json()['job']=="emperor", "job does not match"

pload3={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
p = requests.post('https://reqres.in/api/register', data=pload3)
print(p.json())
print(p.json()["token"])