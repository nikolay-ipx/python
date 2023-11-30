class Point:
    def __init__(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, x1, y1, x2 = 0, y2 = 0):
        if type(x1) == Point and isinstance(y1, Point):
            self.__sp = x1
            self.__ep = y1
        else:
            self.__sp = (x1, y1)
            self.__ep = (x2, y2)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: ({self.__sp[0]}, {self.__sp[1]}) ({self.__ep[0]}, {self.__ep[1]})')

rect = Rectangle(0, 0, 20, 34)
rect.draw()
r1 = Rectangle(Point(1,2), Point(3,4))