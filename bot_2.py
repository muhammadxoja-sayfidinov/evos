import sqlite3
class baza:
    def __init__(self):
        self.con =sqlite3.connect("botning_bazasi.db",check_same_thread=False)
        self.cur=self.con.cursor()
    def create(self):
        self.cur.execute(""" CREATE TABLE evos(
                        mahsulot_id INTEGER ,
                        mahsulot_nomi TEXT,
                        narxi INTEGER
                        )""")
    def call(self,a,):
        self.cur.execute(f"""SELECT narxi FROM evos WHERE mahsulot_id=={a}""")
        temp=self.cur.fetchall()
        for i in temp:
            b= i[0]
            return b
    # print(call()*5)
# new=baza()
# b=new.call()
# print(b*5)

