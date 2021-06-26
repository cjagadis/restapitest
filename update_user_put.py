import requests
import json

pload = {
    "name": "morpheus",
    "job": "Soprano"
}

r = requests.put("https://reqres.in/api/users/2", data=pload)
print(r)
print(r.json())
print(r.json()["job"])
assert r.json()["job"]=='Soprano'

pload2 = {
    "name": "Who knows",
    "job": "Carpenter"
}

r = requests.put("https://reqres.in/api/users/2", data=pload2)
print(r)
print(r.json())
print(r.json()["job"])
assert r.json()["job"]=='Carpenter'

pload3 = {
    "name": "Placido Domingo",
    "job": "Tenor"
}

r = requests.patch("https://reqres.in/api/users/2", data=pload3)
print(r)
print(r.json())
print(r.json()["job"])
assert r.json()["job"]=='Tenor'

pload4= {
    "name": "Pavarotti"
}

r = requests.patch("https://reqres.in/api/users/2", data=pload4)
print(r)
print(r.json())
print(r.json()["name"])
assert r.json()["name"]=='Pavarotti'