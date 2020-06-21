# Multi-Table Database - Tracks

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('music.sqlite')
db = conn.cursor()

create = open('create.sql').read()
db.executescript(create)


def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


tree = ET.fromstring(open('Library.xml').read())  # or tree = ET.parse('Library.xml')
dicts = tree.findall('dict/dict/dict')  # list of all <dict> tags

for entry in dicts:
    if lookup(entry, 'Track ID') is None:
        continue

    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    track = lookup(entry, 'Name')
    length = lookup(entry, 'Total Time')
    rating = lookup(entry, 'Rating')
    count = lookup(entry, 'Play Count')

    if track is None or artist is None or album is None or genre is None:
        continue

    db.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))  # it needs to be tuple
    db.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = db.fetchone()[0]

    db.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    db.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = db.fetchone()[0]

    db.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
    db.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = db.fetchone()[0]

    db.execute('INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)',
               (track, album_id, genre_id, length, rating, count))

conn.commit()
conn.close()

# fetchone()
# Fetches the next row of a query result set, returning a single sequence, or None when no more data is available.
