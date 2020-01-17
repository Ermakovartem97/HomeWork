def check (str):
    str  = str.lower()
    error = 0
    for i in range(len(str) - 1):
        if str[i] == "ж" or str[i] == "ш":
            if str[i + 1] != "и":
                error += 1
        if str[i] == "ч" or str[i] == "щ":
            if str[i + 1] != "а":
                error += 1
    return "У вас ", error, " ошибок"

print(check("Жи и ШИИ а не ЖЫЫ и ЩАА ЧА ЩК"))