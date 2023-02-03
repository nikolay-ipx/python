class PhoneBook:
    def __init__(self, *args):
        self.spisok = list()

    def add_phone(self, phone):
        self.spisok.append((phone.number,phone.fio))

    def remove_phone(self, indx):
        self.spisok.pop(indx)

    def get_phone_list(self):
        return self.spisok

class PhoneNumber:
    def __init__(self, number, fio):
        if type(number) is int and len(str(number)) == 11 and type(fio) is str:
            self.number = numberta
            self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)