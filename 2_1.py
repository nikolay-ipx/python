from accessify import private
class Point:
    aa=1
    bb=2
    def __init__(self, x=0, y=0):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls,x):
        return type(x) in (int,float)

    def set_coord(self,x,y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):
        return self.__x, self.__y

pt = Point(5,6)
pt.set_coord(10, 20)
print(pt.get_coord())
print(pt._Point__x)#доступ к приватному атрибуту