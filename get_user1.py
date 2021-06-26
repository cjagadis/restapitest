import requests

r = requests.get('https://reqres.in/api/users?page=2')

code = r.status_code
print(code)
assert  code==200; "Code does not match"

# show content - json format
print("Json")
print(r.json())

# show headers
print('headers')
print(type(r.headers))
print(r.headers)

# show cookies
print('cookies')
print(r.cookies)

# show encoding
print('encoding')
print(r.encoding)

# show URL
print('URL')
print(r.url)