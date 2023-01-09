class a:
    d = 1
    n = 10

    @classmethod
    def valid(cls, arg):
        return cls.d <= arg <= cls.n

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.valid(x) and self.valid(y):
            self.x = x
            self.y = y
        print(self.norm(self.x, self.y))

    def con(self):
        return self.x, self.y

    @staticmethod
    def norm(x,y):
        return x*x+y*y

b=a(1,2)
print(b.norm(5,6))


