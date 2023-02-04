import requests
import os
import json



API_KEY = "29f05eb0-2754-4686-be13-e563213e5621"
ALL_URL = f"https://api.goperigon.com/v1/all?apiKey={API_KEY}"
extra = "&from=2023-02-01&sourceGroup=top10&showNumResults=true&showReprints=false&excludeLabel=Non-news&excludeLabel=Opinion&excludeLabel=Paid News&excludeLabel=Roundup&excludeLabel=Press Release&sortBy=date&excludeSource=foxnews.com&category=Politics&category=Finance&q=Current World Political News"
extra2 = "&from=2023-02-01&sourceGroup=top10&showNumResults=true&showReprints=false&paywall=false&excludeLabel=Non-news&excludeLabel=Opinion&excludeLabel=Paid News&excludeLabel=Roundup&excludeLabel=Press Release&sortBy=date&excludeSource=foxnews.com&category=Politics&category=Finance&q=Current World Political News"
ALL_URL += extra2

resp = requests.get(f"{ALL_URL}")
article = resp.json()["articles"][0]

print(article["title"])


dic = {}
# print(type(resp.json()["articles"][0]['title']))

for article in resp.json()["articles"]:
    dic[article["title"]] = article["summary"]

cnt = 0
with open("output2.txt", "a") as f:
    for title in dic.keys():
        print(str(cnt) + ": "+  title + "\n", file = f)
        print(str(cnt) + ": "+ dic[title], file = f)
        cnt += 1
    
    
with open("sample.json", "w") as outfile:
    json.dump(dic, outfile)