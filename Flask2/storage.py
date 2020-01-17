import sqlite3

def getCategories():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    result = []
    for row in cursor.execute("""SELECT * FROM categories"""):
        result.append(row[0])
    return {'nameCategory' : result}

def getNameProduct():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    result = []
    for row in cursor.execute("""SELECT * FROM products"""):
        result.append(row[0])
    return {'nameProduct': result}

def getProductCategory(category):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    result = []
    for row in cursor.execute("""SELECT * FROM products WHERE nameCategory = ?""", (category,)):
        result.append(row[0])
    return {'nameProduct': result}

print(getProductCategory('secondCat'))