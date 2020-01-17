import sqlite3

conn = sqlite3.connect("MyDataBase.db")
cursor = conn.cursor()

train_num = input('Введите номер интересующего вас поезда\n')

cursor.execute("SELECT count() FROM buys WHERE train_number = ?", train_num)
print('На выбранный поезд продано : ', cursor.fetchall()[0][0], ' билета.')

cursor.execute("SELECT sum(cost) FROM buys JOIN ticets ON buys.ticet_number = ticets.ticet_number WHERE train_number = ?", train_num)
print('На выбранный поезд продано билетов на сумму: ', cursor.fetchall()[0][0], ' рублей')

cursor.execute("SELECT sum(cost) FROM buys JOIN ticets ON buys.ticet_number = ticets.ticet_number")
print('Всего продано билетов на общую сумму: ', cursor.fetchall()[0][0], ' рублей')

cursor.execute("SELECT count(reys_number) FROM buys JOIN users ON buys.reys_number = users.reys_number")
print(cursor.fetchall())