# open source API - https://reqres.in/ (GET/POST for testing)
# Video: https://www.youtube.com/watch?v=5ZSxk6pX1_0 excellent REST API
# Automation: https://www.youtube.com/channel/UCcTII5pbZYkU4fgFtb4uesg

import requests

r = requests.get('https://reqres.in/api/users?page=2')

# print(r.status_code)
# print(r)
# print(type(r))
# print(dir(r))

code = r.status_code
print(code)
assert  code==200; "Code does not match"
# assert will fail for we are expecting 200
# assert  code==201; "Code does not match" 

# show text - unicode
print("text property")
print(r.text)

# show text - bytoe format
print("content property")
print(r.content)

# show content - json format
print("Json")
print(r.json())