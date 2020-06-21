# Many Students in Many Courses

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

create = open('create.sql').read()
cur.executescript(create)

jsonfile = open('roster_data.json').read()
jsondata = json.loads(jsonfile)

for entry in jsondata:
    name = entry[0]
    course = entry[1]
    role = entry[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (course,))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))

conn.commit()

command = open('command.sql').read()
res = cur.execute(command).fetchone()[0]
print(res)

conn.close()

