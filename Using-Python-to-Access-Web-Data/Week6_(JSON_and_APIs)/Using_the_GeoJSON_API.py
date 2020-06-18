# Using the GeoJSON API

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

parameters = {}
parameters['key'] = 42
parameters['address'] = input('Enter location: ') # address: "University of Delaware"

url = serviceurl + urllib.parse.urlencode(parameters)

data = urllib.request.urlopen(url).read()

info = json.loads(data)

print('Retrieving', url)
print('Retrieved', len(data), 'characters')
print('Place id', info['results'][0]['place_id'])

'''
Whole program in single line
print('Place id', json.loads(urllib.request.urlopen('http://py4e-data.dr-chuck.net/json?' +
                                                    urllib.parse.urlencode({'key': 42, 'address': input('Enter location: ')})).read())['results'][0]['place_id'])
'''