class SingletonFive:
    a=0
    b=None
    def __new__(cls, *args, **kwargs):
        if cls.a < 5:
            cls.a += 1
            cls.b = super().__new__(cls)
        return cls.b

    def __init__(self, name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]
