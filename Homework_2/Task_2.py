def work(n):
    summ = 0
    for i in range(1, n + 1):
        summ += (1./i)
    return summ
print (work(2))