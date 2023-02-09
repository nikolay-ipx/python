class Book:
    a = {'author' : str, 'title' : str, 'pages' : int, 'year' : int}
    def __init__(self, title = '', author = '', pages = 0, year = 0):
        self.author = author
        self.title = title
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if self.a[key] == type(value):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
print(book.author,book.title,book.pages,book.year)
#key in self.a and