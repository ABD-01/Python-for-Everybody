# Extracting Data from XML

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_579175.xml (Sum ends with 10)

xml = urllib.request.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = ET.fromstring(xml)

Sum = 0
counts = tree.findall('comments/comment/count')
print('Count:',len(counts))
for count in counts:
    Sum += int(count.text)

print('Sum:', Sum)

# Whole program in one line
# print('Sum:', sum([int(count.text) for count in ET.fromstring(urllib.request.urlopen(url = input('Enter location: ')).read()).findall('comments/comment/count')]))