from math import sqrt

class myExeption(Exception):
    pass

def findS(p, a, b, c):
    return (sqrt(p * (p - a) * (p - b) * (p - c)))
def findP(a, b, c):
    return ((a + b + c) / 2)
def myInput():
    a = input("Введите a: ")
    b = input("Введите b: ")
    c = input("Введите c: ")
    if a.isalpha() or b.isalpha() or c.isalpha():
        raise myExeption("Вы ввели не число")
    a = int(a)
    b = int(b)
    c = int(c)
    if a < 0 or b < 0 or c < 0:
        raise myExeption("Длинна не может быть отрицательной")
    return ([a, b, c])

try:
    st = myInput()
    P = findP(st[0], st[1], st[2])
    S = findS(P, st[0], st[1], st[2])
    print("Площадь треугольника: ", S)
except myExeption as ex:
    print(ex)