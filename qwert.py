class Point:
    def __init__(self,a):
        self.xx=a

    @classmethod
    def izi(cls,coord):
        if type(coord) != int:
            raise TypeError ('sdfsfsdgs')
    @property
    def xx(self):
        return self.a
    @xx.setter
    def xx(self, value):
        self.izi(value)
        self.a = value

e=Point(5)
print(e.__dict__)




