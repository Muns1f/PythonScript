import requests
import re
import sys

if len(sys.argv) < 2:
    print("[+] Usage: python3 scrapEmails.py http://example.com")
else:
    url = sys.argv[1]

    req = requests.get(url,"html.parser").text



    regexgValue = re.findall("\S{1,}@[A-z0-9]{1,}\.[A-z0-9]{1,}",req)

    for email in regexgValue:
        f = open("EmailsFromScrapping.txt","a")
        f.write(email)
        f.write("\n")
        f.close()
        print(email)
