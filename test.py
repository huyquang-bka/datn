from Database.utils import Database

db = Database()
dictionary = {'id': 2, 'plate': '30F67330', 'color': 'silver', 'brand': 'Nissan', 'img_path': 'ImageStorage/1.jpg'}
db.insert_to_db(dictionary)

# insert into parking values(1, '30F67330', 'SILVER', 'NISSAN', '2022-06-16 23:15:41', 'None', 'ImageStorage/1.jpg')
