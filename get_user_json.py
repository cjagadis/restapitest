import requests
import json
import timeit

start = timeit.timeit()
r = requests.get('https://reqres.in/api/users?page=2')
end = timeit.timeit()
print('Get time')
print(end - start)

# print(r.status_code)
# print(r)
# print(type(r))
# print(dir(r))

json_1 = '{"page":2,"per_page":6,"total":12,"total_pages":2,\
    "data":[{"id":7,"email":"michael.lawson@reqres.in","first_name":"Michael",\
    "last_name":"Lawson","avatar":"https://reqres.in/img/faces/7-image.jpg"},\
    {"id":8,"email":"lindsay.ferguson@reqres.in","first_name":"Lindsay","last_name":"Ferguson",\
    "avatar":"https://reqres.in/img/faces/8-image.jpg"},{"id":9,"email":"tobias.funke@reqres.in",\
    "first_name":"Tobias","last_name":"Funke","avatar":"https://reqres.in/img/faces/9-image.jpg"},\
    {"id":10,"email":"byron.fields@reqres.in","first_name":"Byron","last_name":"Fields",\
    "avatar":"https://reqres.in/img/faces/10-image.jpg"},{"id":11,"email":"george.edwards@reqres.in",\
    "first_name":"George","last_name":"Edwards","avatar":"https://reqres.in/img/faces/11-image.jpg"},\
    {"id":12,"email":"rachel.howell@reqres.in","first_name":"Rachel","last_name":"Howell",\
    "avatar":"https://reqres.in/img/faces/12-image.jpg"}],\
    "support":{"url":"https://reqres.in/#support-heading",\
    "text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}'

print("json_1")
print(json_1)

code = r.status_code
print(code)
assert  code==200; "Code does not match"

# show content - json format
print("Json_2")
print(r.json())

json_2 = r.text

# Compare two jsons
json_dict1 = json.loads(json_1)
json_dict2 = json.loads(json_2)

print(sorted(json_dict1.items()) == sorted(json_dict2.items()))