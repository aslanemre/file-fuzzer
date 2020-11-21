# -*- coding: utf-8 -*-

import requests

## url must be like > http(s)://subdomain.domain.tld/

url = str(input("[ ? ] Url : "))

print("[ * ] Files Scanning...")
    
print("")

files = ["index.php","index.html","admin.html","admin.php",
        "robots.txt","index.asp","index.aspx","admin.asp",
        "admin.aspx","search.php","config.txt","login.php",
        "signin.php","signup.php",".DS_Store","phpinfo.php",
        "admin.txt",".htaccess",".htpasswd",".backup",
        ".conf",".config",".env",".git","id_rsa","id_rsa.txt",
        ".svn","administrator.php","config.php","cmd.php",
        "user.html","user.php","dash.php","dashboard.php",
        ".install","install.php","creds.txt","credentials.txt",
        ".id_rsa","go.php","run.php","url.php","redirect.php",
        "view.php","file.php","open.php","db.txt","db.php","database.txt",
        "database.php",".sql",".db","sql.txt","export.php","import.php",
        "dir.php","directory.php","form.php","save.php","settings.txt",
        "settings.php","profile.php","my.php","base.php","key.php",
        "auth.php","connect.php","return.php","back.php"]


for file in files:
    
    urlfile = url+file
    
    response = requests.get(url=urlfile, allow_redirects=False, verify=True)
    
    if str(response.status_code) == "301":
        print("[ + ]", file, response.status_code)
    elif str(response.status_code) == "200":
        print("[ + ]", file, response.status_code)
    elif str(response.status_code) == "302":
        print("[ + ]", file, response.status_code)
    elif str(response.status_code) == "403":
        print("[ + ]", file, response.status_code)
    elif str(response.status_code) == "401":
        print("[ + ]", file, response.status_code)
    elif str(response.status_code) == "201":
        print("[ + ]", file, response.status_code)