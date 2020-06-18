# Extracting Data from JSON

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_579176.json (Sum ends with 18)

data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('Count:', len(info['comments']))

Sum = 0
for comment in info['comments']:
    Sum += int(comment['count'])

print('Sum', Sum)

# Program in Single Line
# print('Sum', sum([int(i['count']) for i in json.loads(urllib.request.urlopen(url = input('Enter location: ')).read())['comments']]))