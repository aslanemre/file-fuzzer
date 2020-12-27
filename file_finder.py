# -*- coding: utf-8 -*-

import requests

url = str(input("[ ? ] Url : "))

print("[ * ] Files Scanning...")
    
print("")

files = open("list.txt","r")


for file in files.readlines():
    
    urlfile = url+file
    
    response = requests.get(url=urlfile, allow_redirects=False, verify=True)
    
    if str(response.status_code) == "301":
        print("[ 301 ]", file)
    elif str(response.status_code) == "200":
        print("[ 200 ]", file)
    elif str(response.status_code) == "302":
        print("[ 302 ]", file)
    elif str(response.status_code) == "403":
        print("[ 403 ]", file)
    elif str(response.status_code) == "401":
        print("[ 401 ]", file)
    elif str(response.status_code) == "201":
        print("[ 201 ]", file)

print("")

print("[ = ] Scan Finished! ")

print("")

files.close()