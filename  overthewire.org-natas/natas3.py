#!/usr/bin/env python3
import requests 
import re

username = "natas3"
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

s = requests.session()

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username

r = s.get(url, auth = (username, password))
content = r.text
# print(content)
print(re.findall('natas4:(.*)',content)[0])