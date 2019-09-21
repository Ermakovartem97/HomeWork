def parking(day, hour):
    hour = int(''.join(filter(str.isdigit, hour)))
    if hour > 1900 and hour < 2059:
        return("Both")
    elif day % 2 == 0 and hour > 2100 or day % 2 == 1 and hour < 1859:
        return ("Left")
    else:
        return ("Right")

print(parking(4,"22:50"))
print(parking(5,"22:50"))
print(parking(5,"19:50"))
print(parking(5,"00:50"))
print(parking(6,"00:50"))


