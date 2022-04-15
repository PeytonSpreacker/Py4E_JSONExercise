import urllib.request
import json

url = input('Enter a url: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_1501844.json'

print('Retrieving', url)

data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters.')

info = json.loads(data)
# print(json.dumps(info, indent=4))

print(len(data), 'characters found.')

tot = []

for i in info['comments']:
    tot.append(i['count'])

print('Sum: ', sum(tot))