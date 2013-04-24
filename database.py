
import sqlite3

# TODO
#  - Clean of db


DBPATH = '/home/jonathan/forward/db.sqlite'


def insert(alias, addr, expire):
    conn = sqlite3.connect(DBPATH)
    c = conn.cursor()
    c.execute('INSERT INTO aliases VALUES(?,?,?)',(alias,addr,expire))
    conn.commit()
    c.close()

def getPersistentAlias(addr):
    conn = sqlite3.connect(DBPATH)
    c = conn.cursor()
    c.execute("SELECT alias FROM aliases WHERE forw_addr = ? AND expire = '9999-01-01 00:00:00'",(addr,))
    
    alias = False
    for r in c:
        alias = r[0]
        break

    c.close()

    return alias

def aliasExists(alias):
    conn = sqlite3.connect(DBPATH)
    c = conn.cursor()
    c.execute("SELECT alias FROM aliases WHERE alias = ?",(alias,))
    
    exists = False
    for r in c:
        exists = True
        break

    c.close()

    return exists

if __name__=="__main__":
    print getPersistentAlias('the9ull@silix.org')
    print aliasExists('fw-hypothesiser-catalyser-810526a6f392')
    print aliasExists('fw-cacca')
