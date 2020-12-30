# -*- coding: utf-8 -*-

import sys
import requests
from colorama import Fore, Back, Style 
from fake_useragent import UserAgent


def dirFuzzing():

    url = str(input(Fore.CYAN + "[ ? ] Url : "))

    print(Fore.CYAN + "[ - ] Files Scanning...")
    
    print("")

    files = open("list.txt","r")

    for file in files.readlines():

        urlfile = url+file

        try:
            user_agent = UserAgent()
            useragent = user_agent.random
        except FakeUserAgentError:
            pass
    
        try:
            response = requests.get(url=urlfile, allow_redirects=False, verify=True, headers={'User-Agent': useragent})
    
            if str(response.status_code) == "301":
                print(Fore.YELLOW + "[ 301 ]", file)

            elif str(response.status_code) == "200":
                print(Fore.GREEN + "[ 200 ]", file)

            elif str(response.status_code) == "302":
                print(Fore.YELLOW + "[ 302 ]", file)

            elif str(response.status_code) == "201":
                print(Fore.GREEN + "[ 201 ]", file)
        except requests.ConnectionError:
            print(Fore.RED + "[ ! ] Connection Error. Try again.")
            print("")
            dirFuzzing()

    print("")

    print(Fore.RED + "[ = ] Scan Finished! ")

    print("")

    files.close()

dirFuzzing()
