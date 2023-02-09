# class Point:
#     a=None
#     def __new__(cls, *args, **kwargs):
#         if cls.a is None:
#             cls.a = super().__new__(cls)
#         return cls.a
#
#     def __del__(self):
#         Point.a=None
#
#     def __init__(self,x=0,y=0):
#         print('it s init'+ str(self))
#         self.x=x
#         self.y=y
#
#     def connect(self):
#         print(f'{self.x},{self.y}')
#
# bd=Point(1,2)
# bd2=Point(3,4)
# bd.connect()
# bd2.connect()

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
for i in objs:
    print(id(i),i.name,i)
