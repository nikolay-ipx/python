#дескрипторы

#дескриптор не данных
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


#дескриптор данных (data descriptor)
class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name): #self-ссылка на создоваемый экземпляр класса Integer
                                         #owner-ссылка на класс Point3D
                                         #name-имя экземплара класса
        self.name = "_" + name # создание локального атрибута

    def __get__(self, instance, owner): #self-ссылка экземпляр класса Integer
                                        #instance-ссылка на экземпляр класса Point3D
                                        #owner-ссылка на класс Point3D
        #return instance.__dict__[self.name] #1 вариант
        return getattr(instance, self.name) #2 вариант

    def __set__(self, instance, value): #self-ссылка экземпляр класса Integer
                                        #instance-ссылка на экземпляр класс Point3D
                                        #value-присваемое значение
        print(f"__set__: {self.name} = {value}")
        self.verify_coord(value)
        #instance.__dict__[self.name] = value #1 вариант
        setattr(instance, self.name, value) #2 вариант


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

pt = Point3D(1, 2, 3)
print(pt.xr, pt.x)
print(pt.__dict__)
