import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS categories
                  (nameCategory text);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS makers
                  (nameMaker text);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS comments
                  (user text, commentText text, rating integer);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS sales
                  (data text, user text, salesBuy text, sum float);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS products
                  (nameProduct text, image text, profile text, character text, cost float, nameCategory text, nameMaker text, new integer, commentText text );""")

categories = [('firstCat',), ('secondCat',)]
cursor.executemany("INSERT INTO categories (nameCategory) values (?)", categories)

products = [('1','https://upload.wikimedia.org/wikipedia/commons/8/87/TVE_La1_-_Logo_2008.png','Это 1','01', '1', 'firstCat', 'firstMak', '1', 'Коментарий'),
            ('2','https://upload.wikimedia.org/wikipedia/commons/7/75/Logo_TVE-2.svg','Это 2','02', '2', 'firstCat', 'secondMak', '0', 'Коментарий2'),
            ('3','https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/NYCS-bull-trans-3.svg/1024px-NYCS-bull-trans-3.svg.png','Это 3','03', '3', 'secondCat', 'firstMak', '3', 'Коментарий3'),]
cursor.executemany("INSERT INTO products (nameProduct, image, profile, character, cost, nameCategory, nameMaker, new, commentText) values (?,?,?,?,?,?,?,?,?)", products)

conn.commit()