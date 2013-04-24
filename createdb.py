
import sqlite3

conn = sqlite3.connect('/home/jonathan/forward/db.sqlite')

c = conn.cursor()

c.execute('''CREATE TABLE aliases
(alias text, forw_addr text, expire text)''')

#c.execute('''INSERT INTO aliases VALUES(?,?,?)''',t)

conn.commit()

c.close()
