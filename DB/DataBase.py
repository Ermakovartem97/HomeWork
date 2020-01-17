import sqlite3

conn = sqlite3.connect("MyDataBase.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (name TEXT, surname TEXT, reys_number INTEGER NOT NULL PRIMARY KEY);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS trains (train_number INTEGER NOT NULL PRIMARY KEY, way TEXT, data TEXT);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS ticets (ticet_number INTEGER NOT NULL PRIMARY KEY, cost INTEGER);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS buys (reys_number INTEGER, train_number INTEGER, ticet_number INTEGER);
""")

users_value = [('Kiril', 'Petrov', 1), ('Ivan', 'Shemetov', 2), ('Misha', 'Revin', 3)]
cursor.executemany("INSERT INTO users (name, surname, reys_number) values (?, ?, ?)", users_value)

trains_value = [(1, 'SPB-MSC', '11.11.19'), (2, 'MSC-SPB', '14.10.19'), (3, 'BRY-SPB', '2.11.19'), (4, 'SPB-BRY', '30.11.19'), (5, 'BRY-MSC', '7.10.19')]
cursor.executemany("INSERT INTO trains (train_number, way, data) values (?, ?, ?)", trains_value)

ticets_value = [(1, 3000), (2, 4000)]
cursor.executemany("INSERT INTO ticets (ticet_number, cost) values (?, ?)", ticets_value)

buys_value = [(1, 5, 2), (2, 2, 1), (1, 4, 1), (3, 1, 2), (2, 3, 2), (3, 5, 2), (1, 1, 2)]
cursor.executemany("INSERT INTO buys (reys_number, train_number, ticet_number) values (?, ?, ?)", buys_value)

conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
cursor.execute("SELECT * FROM trains")
print(cursor.fetchall())
cursor.execute("SELECT * FROM ticets")
print(cursor.fetchall())
cursor.execute("SELECT * FROM buys")
print(cursor.fetchall())


