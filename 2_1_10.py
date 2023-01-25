import random
from string import ascii_lowercase, digits

class EmailValidator:
    CHARS = ascii_lowercase + digits + '_' + '.'
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        cls.email = [[x for x in random.choice(cls.CHARS)] for x in random.randrange(1,100)]