class Point:
    __name = 1
    __old = 2
    @property
    def name1(self):
        return self.__name
    @name1.setter
    def name1(self,name):
        self.__name = name

    @name1.deleter
    def name1(self):
        del self.__name


