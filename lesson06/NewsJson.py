import json
import requests

news_list = []
url = 'http://oldpaper.g0v.ronny.tw/index/json?fbclid=IwAR1zip-1_wLBrsZ2p9RfiAjm-WeFaxb8UyI4nA-uXOhK6Q3Wkgn7D_Zukow'
data = json.loads(requests.get(url).text)

for d in data.get('data'):
    dict = {'title':d.get('title'), 'headlines':d.get('headlines')}
    news_list.append(dict)

file = open('news.txt','a')
for news in news_list:
    for head in news['headlines']:
        if '譚' in head[1]:
            print(head)
            file.write(head[1])
