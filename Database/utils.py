import sqlite3


conn = sqlite3.connect('Database/huyquang.db')
c = conn.cursor()

def get_info(search_dict):
    result_dict = {}
    plate = search_dict['plate'].strip().upper()
    color = search_dict['color'].strip().upper()
    brand = search_dict['brand'].strip().upper()
    if plate:
        command = f"select * from parking where plate={plate}"
    elif color and brand:
        command = f"select * from parking where color='{color}' and brand='{brand}'"
    elif color:
        command = f"select * from parking where color='{color}'"
    elif brand:
        command = f"select * from parking where brand='{brand}'"
    else:
        return result_dict
    print(command)
    c.execute(command)
    columns = c.fetchall()
    for column in columns:
        id, plate, color, brand, in_time, out_time, img_path = column
        result_dict[id] = {'plate': plate, 'color': color, 'brand': brand, 'in_time': in_time, 'out_time': out_time, 'img_path': img_path}
        break
    return result_dict