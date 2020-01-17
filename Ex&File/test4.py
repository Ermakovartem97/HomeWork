
class myCsv:
    name = ''
    sep = ';'

    def __init__(self, newName, newSep = ';'):
        self.name = newName
        self.sep = newSep

    def readAll(self):
        content = []
        with open(self.name + '.csv', 'r') as file:
            for i in file:
                content.append(i[:-1].split(self.sep))
        return(content)





file = myCsv('test')
print(file.readAll())