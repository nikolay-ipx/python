from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    @staticmethod
    def check_card_number(number):
        a = True
        if len(number.replace('-','')) != 16:
            a = False
        else:
            for i in number.replace('-',''):
                if i not in digits:
                    a = False
                    break
        return a



    @staticmethod
    def check_name(name):
        a = True
        if len(name.split()) != 2:
            a = False
        else:
            for i in name.replace(' ',''):
                if i not in CardCheck.CHARS_FOR_NAME:
                    a = False
                    break
        return a

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_number)
print(is_name)
