# Following Links in HTML Using BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter the url - ')
count = int(input('Enter count: '))
pos = int(input('Enter position: ')) - 1

for i in range(count):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pos].get('href', None)
print(f'The answer to the assignment for this execution is "{tags[pos].contents[0]}"')

'''
Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Manar.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: G
'''
