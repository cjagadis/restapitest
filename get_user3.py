import requests

p = {"page":2}
r = requests.get('https://reqres.in/api/users', params=p)
print(r.url)

# Json response
js_resp=r.json()

print(js_resp['total'])
assert js_resp['total']==12

print(js_resp['total_pages'])
assert js_resp['total_pages']==2, "total pages count does not match"

print(js_resp["data"][0]["email"])
assert (js_resp["data"][0]["email"]).endswith("reqres.in"), "email format does not match"

print(js_resp["data"][0]["first_name"])
assert (js_resp["data"][0]["first_name"])!=None, "first name does not match"

print(js_resp["data"][2]["last_name"])
assert (js_resp["data"][2]["last_name"])!=None, "last name does not match"

print(js_resp["support"]["url"])
