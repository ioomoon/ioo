#hello

import requests
import re

result = False

link1 = input()
res1 = requests.get(link1)
if res1.status_code == 200:
    link2 = input()
    for link in re.findall(r"<a href=\"(.*)\"", res1.text):
        res = requests.get(link)
        if res.status_code == 200:
            for url in re.findall(r"<a href=\"(.*)\"", res.text):
                if url == link2:
                    result = True
                    break
            if result:
                break
else:
    result = False


if result:
    print("Yes")
else:
    print("No")

