class AbstractClass:
    a=True
    def __new__(cls, *args, **kwargs):
        if cls.a is True:
            return "Ошибка: нельзя создавать объекты абстрактного класса"
obj = AbstractClass()
print(obj)