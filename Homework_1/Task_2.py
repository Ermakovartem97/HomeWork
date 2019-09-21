def palindrom (n):
    s = str(n)
    if len(s) <= 2:
        return (print("Это не палиндром"))
    if len(s) == 3:
        s = "0" + s
    if (int(s[0]) + int(s[1])) == (int(s[2]) + int(s[3])):
        print("Это палиндром")
    else:
        print("Это не палиндром")

palindrom(1242)
palindrom(1221)
palindrom(330)
palindrom(10)