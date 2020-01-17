#x = input('Введите первое число для вычитания оно должно быть больше второго')
#y = input('Введите второе число для вычитания')

def myMinus(a, b):
    k = []
    if a < b:
        k.append(True)
        k.append(a + 10 - b)
    else:
        k.append(False)
        k.append(a - b)
    return(k)

def myPlus(a, b):
    k = []
    if a + b >= 10:
        k.append(True)
        k.append((a + b) % 10)
    else:
        k.append(False)
        k.append(a + b)
    return(k)


x = [2, 1]
y = [6]
minLen = min(len(x), len(y))
maxLen = max(len(x), len(y))
ans = []

for i in range(1, minLen + 1):
    prov = myMinus(x[-i], y[-i])
    if prov[0]:
        x[-i - 1] -= 1
    ans.append(prov[1])

for i in range(minLen, maxLen):
    if x[-i-1]>= 0:
        ans.append(x[-i-1])
    else:
        ans.append(9)
        x[-i-2] -= 1

j = 0
for i in ans[::-1]:
    j += 1
    if i != 0:
        ans = ans[-j::-1]
        break
print('x - y = ', ans)

#x = input('Введите первое число для сложения')
#y = input('Введите второе число для сложения')

x = [7]
y = [6]
ans = []
x.append(0)
x = x[::-1]
minLen = min(len(x), len(y))
maxLen = max(len(x), len(y))

for i in range(1, minLen + 1):
    prov = myPlus(x[-i], y[-i])
    if prov[0]:
        x[-i - 1] += 1
    ans.append(prov[1])

for i in range(minLen, maxLen):
    if x[-i-1] < 10:
        ans.append(x[-i-1])
    else:
        ans.append(0)
        x[-i-2] += 1

j = 0
for i in ans[::-1]:
    j += 1
    if i != 0:
        ans = ans[-j::-1]
        break
print('x + y = ', ans)