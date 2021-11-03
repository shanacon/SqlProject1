import sqlite3 as lite
def NewType(TypeName) :
    con = lite.connect('FileData.db')
    with con:
        cur=con.cursor()
        cur.execute(f"Insert into TYPE Values(null, '{TypeName}')")