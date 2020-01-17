a = [2, 'cat', 7, 2, 9, 'cat', 7, 42]
print(a)
i = 0
b = []
for it in a:
    i += 1
    f = True
    for it2 in a[i:]:
        if it == it2:
            f = False
    if f:
        b.append(it)
print(b)