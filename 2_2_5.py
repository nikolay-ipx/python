class WindowDlg:
    def __init__(self, title, width, height ):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,chir):
        if type(chir) is int and 0 <= chir <= 10000:
            self.__width = chir
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, vis):
        if type(vis) is int and 0 <= vis <= 10000:
            self.__height = vis
            self.show()

a=WindowDlg('ghbdtn', 1, 2)
a.show()
a.height = 5