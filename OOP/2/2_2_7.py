class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x = 0, y = 0):
        self.__x = 0
        self.__y = 0
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y

a = RadiusVector2D(-101,2000)
print(a.x)
print(a.y)
a.x = 1025
a.y = -101
print(a.x)
print(RadiusVector2D.norm2(a))

