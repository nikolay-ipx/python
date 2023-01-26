import random
from string import ascii_lowercase, digits

class EmailValidator:
    CHARS = ascii_lowercase + digits + '_' + '.'
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        cls.email = ''.join([random.choice(cls.CHARS) for i in range(random.randint(1,100))])+'@gmail.com'
        return cls.email

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            if email.count('@') != 1 or email.count('..') != 0:
                return False
            for i in email:
                if i not in cls.CHARS and i not in '_@.':
                    return False
            em = email.split('@')
            if len(em[0]) >= 100 or len(em[1]) >= 50 or em[1].find('.') == -1:# or em[1].count('..') != 0:
                return False

        return True

    @staticmethod
    def __is_email_str(email):
        if type(email) is str:
            return True
        else:
            return False





# print(EmailValidator.get_random_email())
print(EmailValidator.check_email("sc_lib@list_ru"))
print(EmailValidator.check_email("sc@lib@list_ru"))
print(EmailValidator.check_email("sc.lib@list_ru"))
print(EmailValidator.check_email("sclib@list.ru"))
print(EmailValidator.check_email("sc.lib@listru"))
print(EmailValidator.check_email("sc..lib@list.ru"))