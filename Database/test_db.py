import sqlite3

conn = sqlite3.connect('Database/huyquang.db')
c = conn.cursor()

c.execute("select * from parking")
datas = c.fetchall()
for data in datas:
    print(data)

