import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        return self.lst_data[a-1:b]

    def insert(self, data):
        for i in data:
            self.lst_data.append(dict(zip(self.FIELDS,i.split())))


db = DataBase()
db.insert(lst_in)
print(DataBase.__dict__)
print(db.select(1,4))
