import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('../../db/test.sqlite3')
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print(type(data)," : ",data)
    print("SQLite version: %s" % data)

    with con:
        if cur is not None:
            cur = con.cursor()
        try:
            cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
            cur.execute("INSERT INTO Users VALUES(1,'Michelle')")
            cur.execute("INSERT INTO Users VALUES(2,'Sonya')")
            cur.execute("INSERT INTO Users VALUES(3,'Greg')")
        except lite.Error as e:
            print("Error %s:" % e.args[0])

        cur.execute("SELECT id,name FROM Users")
        rows = cur.fetchall()
        for row in rows: print(row)

except lite.Error as e:
    print("Error %s:" % e.args[0])
    sys.exit(1)
finally:
    if con: con.close()