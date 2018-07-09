#!/usr/bin/python
# coding: UTF-8
import sqlite3

db = sqlite3.connect('database.db')
c = db.cursor()
stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]
c.executemany('INSERT INTO portfolio VALUES (?,?,?)', stocks)
for row in db.execute('SELECT * FROM portfolio'):
    print row
