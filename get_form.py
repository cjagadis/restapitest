import requests
from requests.structures import CaseInsensitiveDict
import difflib
import sys


url = "https://reqbin.com/echo/post/form"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "key1=value1&key2=value2"

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

with open('output_1_html', 'w') as outfile:
   outfile.write(resp.text)

in_html = open('input_1_html', 'U').readlines()
ou_html = open('output_1_html', 'U').readlines()

diff = difflib.HtmlDiff().make_file(in_html, ou_html, 'input_1_html', 'output_1_html')
sys.stdout.writelines(diff)