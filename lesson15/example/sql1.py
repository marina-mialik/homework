import sqlite3

con = sqlite3.connect('lesson15\\example\\test2.db')
cur = con.cursor()


# sql = \
# """CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         fname TEXT,
#         lname TEXT,
#         gender TEXT,
#         age INTEGER NOT NULL);
# """

# cur.execute(sql)
# con.commit()


# sql = """
# CREATE TABLE IF NOT EXISTS phone_numbers (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     phone_type TEXT NOT NULL,
#     number TEXT(20) NOT NULL,
#     user_id INTEGER NOT NULL,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# );"""

# cur.execute(sql)
# con.commit()

# # посмотреть список таблиц
# cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cur.fetchall())

# -----------------------------------

# # CRUD - 
# Create (Создание): операция добавления новых записей в базу данных.
# Read (Чтение): операция извлечения данных из базы данных.
# Update (Обновление): операция изменения существующих записей в базе данных.
# Delete (Удаление): операция удаления записей из базы данных

# ---------- создание данные ------

# так нельзя
# input_data = "Max"
# sql = f"""
# INSERT INTO users (fname, lname, gender, age)  
# VALUES ('qq','{input_data}','asa',22)" # так нельзя

# добавляем только через слоты - ?
# sql1 = "INSERT INTO users (fname, lname, gender, age)  VALUES (?,?,?,?)"
# cur.execute(sql1, ['Max', 'Maxov', 'm', 15])

# sql2 = "INSERT INTO users (fname,  age)  VALUES (?,?)"
# cur.execute(sql2, ['Paule', 20])
# con.commit()

# records = [
#     ("John", "Doe", "Male", 30),
#     ("Jane", "Smith", "Female", 25),
#     ("Michael", "Brown", "Male", 40),
#     ("Emily", "Johnson", "Female", 28),
#     ("William", "Davis", "Male", 35)
# ]
# cur.executemany(sql1, records)
# con.commit()

# records = [
#     ("Мобильный", "+7 900 123 45 67", 1),
#     ("Рабочий", "+7 495 123 45 67", 1),
#     ("Домашний", "+7 812 123 45 67", 2),
#     ("Мобильный", "+7 916 123 45 67", 2),
#     ("Рабочий", "+7 499 123 45 67", 2),
#     ("Домашний", "+7 812 987 65 43", 5),
#     ("Мобильный", "+7 905 123 45 67", 3),
#     ("Рабочий", "+7 495 987 65 43", 7),
#     ("Домашний", "+7 812 111 22 33", 4),
#     ("Мобильный", "+7 916 987 65 43", 9),
#     ("Рабочий", "+7 499 111 22 33", 10),
#     ("Домашний", "+7 812 444 55 66", 11),
# ]
# sql3 = "INSERT INTO phone_numbers (phone_type, number, user_id)  VALUES (?,?,?)"

# cur.executemany(sql3, records)
# con.commit()


# ----------------- чтение -----------

# sql = "SELECT fname, gender FROM users"
# sql = "SELECT fname FROM users"
# sql = "SELECT * FROM users"

# sql = r"""
# SELECT lname, age 
# FROM users 
# WHERE gender='Male' and (fname LIKE '%i%' OR age < 18) 
# ORDER BY fname 
# LIMIT 10"""


# sql = """
# SELECT u.fname, t.phone_type, t.number 
# FROM users as u,  phone_numbers as t
# WHERE u.id = t.user_id
# """


# все пользователи с телефонами - даже если нет телефона
# sql = """
# SELECT u.fname, t.phone_type, t.number 
# FROM users as u
# LEFT JOIN phone_numbers as t ON u.id = t.user_id
# """

# # все телефоны с пользователями 
# sql = """
# SELECT u.fname, t.phone_type, t.number 
# FROM users as u
# JOIN phone_numbers as t ON u.id = t.user_id
# """


# cur.execute(sql)
# # data = cur.fetchone()
# data = cur.fetchall()
# print(*data, sep='\n')
# # con.close()



# ------- обновление ----

# query = """
# UPDATE users 
# SET fname = 'Maximilian', age = 44
# WHERE id = 1"""
# cur.execute(query)

# updates = [
#     ("Мобильный", "+7 916 123 45 77", 1),  
#     ("Рабочий", "+7 499 987 65 43", 2),   
#     ("Домашний", "+7 812 444 55 66", 3),  
# ]

# for update in updates:
#     query = """UPDATE phone_numbers 
#                 SET phone_type = ?, number = ?
#                 WHERE user_id = ?"""
#     cur.execute(query, update)

# con.commit()
# print(*cur.execute("SELECT * FROM phone_numbers").fetchall(), sep="\n")


# # ------- удаление ----
    
# query = """DELETE FROM users WHERE id = 77"""
# cur.execute(query)
# con.commit()



con.close()