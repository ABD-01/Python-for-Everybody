# Scraping HTML Data with BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen(input('Enter the url - ')).read()
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_579173.html (Sum ends with 82)

soup = BeautifulSoup(html, 'html.parser')

Sum = 0
tags = soup('span')
for tag in tags:
    Sum += int(tag.contents[0])

print('Count', len(tags))
print('Sum', Sum)

# In one line
# print('Sum', sum([int(tag.contents[0]) for tag in BeautifulSoup(urllib.request.urlopen(input('Enter the url - ')).read(), 'html.parser')('span')]))


'''
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs
'''