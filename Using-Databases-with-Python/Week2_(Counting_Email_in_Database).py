# Counting Email in a Database

import sqlite3
import re

conn = sqlite3.connect('email.sqlite')
db = conn.cursor()

db.execute('DROP TABLE IF EXISTS Counts')
db.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

counts = dict()
file = 'mbox.txt' # http://www.py4e.com/code3/mbox.txt
orgs = re.findall('From .*@(\S*)', open(file).read())
for org in orgs:
    counts[org] = counts.get(org, 0) + 1
for org, count in counts.items():
    db.execute("INSERT INTO Counts (org, count) VALUES (?, ?)", (org, count))

conn.commit()
conn.close()