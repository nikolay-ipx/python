class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        '''автоматически вызывается когда идет обращение к атрибуту экземпляра класса,
        возвращает атрибут экземпляра класса к которому идет обращение'''
        # print('__getattribute__')
        # return object.__getattribute__(self, item)
        # пример, запрет доступа к атрибуту
        if item == 'x':
            raise ValueError('Доступ закрыт')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        '''автоматически вызывается когда иде присвоение атрибута экземплара класса
        key - имя атрибута, value - значение атрибута'''
        # пример запрета создания локального атрибута экземпляра класса с определенным именем
        if key == 'z':
            raise AttributeError('недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)# 1 вариант
            #self.__dict__[key] = value# 2 вариант
            #super.__setattr__(key,value)# 3 вариант

    def __getattr__(self, item):
        '''Запускается автоматически когда идет обращение
        к несуществующему атрибуту экземпляра класса
        Если метод не обозначить, то при обращении к
        несуществующему атрибуту появится ошибка'''
        print('__getattr__ ' + item)
        return False

    def __delattr__(self, item):
        ''' вызывается всякий раз когда удаляется атрибут экземпляра класса'''
        print('__delattr__' + item)
        object.__delattr__(self, item)
p1 = Point(1,2)
p2 = Point(3,4)
print(p1.__dict__)
del p1.x
print(p1.__dict__)

