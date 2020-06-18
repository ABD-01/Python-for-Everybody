# Extracting Data With Regular Expressions

import re

print(sum([int(n) for n in re.findall('[0-9]+', open(input('Enter the filename: '), 'r').read())]))