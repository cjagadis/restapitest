import requests
import json

# httpbin delay API
r = requests.get("https://httpbin.org/delay/3", timeout=5)
print(r.status_code)