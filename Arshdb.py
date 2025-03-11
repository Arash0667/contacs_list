import sqlite3

class Database:
    def __init__(self,db):
        self.con= sqlite3.connect(db)
        self.cur= self.con.cursor()
        self.cur.execute( """        
                            CREATE TABLE IF NOT EXISTS Contacts (id integer PRIMARY KEY,
                            name text, family text , address real , phone integer)
                            """)
        self.con.commit()

    def insert(self,name,family,address,phone):
        self.cur.execute('INSERT INTO Contacts VALUES (null,?,?,?,?)',(name,family,address,phone))
        self.con.commit()

    def select_records (self):
        self.cur.execute('SELECT * FROM Contacts ' )
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM Contacts WHERE id = ?",(id,))
        self.con.commit()

    def update(self, id ,name,family,address,phone):
        self.cur.execute( """
                        UPDATE Contacts SET name = ? , family = ?,address = ?, phone=? WHERE id = ?  
                        """ ,(name,family,address,phone,id))
        self.con.commit()

    def search(self, name):
        self.cur.execute('SELECT * FROM Contacts WHERE id=? or name =? or family=? or address= ? or phone =? ',(name,name,name,name,name))
        recs = self.cur.fetchall()
        return recs



db1= Database("D:/Arashpyt/dbproject.db")
# db1.insert_records("Arash","Abedi","Arak","0918")
# result = db1.select_records()
# for rec in result:
#     print(rec)
