from math import sqrt
def mySqrt(x):
    return (sqrt(x))

x = input("Введите чило: ")
try:
    x = int(x)
    print(mySqrt(x))
except ValueError as ex:
    print("Некоректное значение")
    if str(x).isalpha():
        print("Это не число")
    elif x < 0:
        print("Число меньше 0")