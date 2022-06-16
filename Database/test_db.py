import sqlite3

conn = sqlite3.connect('huyquang.db')
c = conn.cursor()

c.execute("""insert into parking values(1, '0F673385', 'SILVER', 'NISSAN', '2022-06-16 23:07:10', 'None', 'ImageStorage/1.jpg')
""")

