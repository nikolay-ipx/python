class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    a = 1
    b = {'name' : (str, ), 'weight' : (float, int), 'price' : (int, )}
    def __init__(self, name, weight, price):
        # self.id = 1
        self.name = name
        self.weight = weight
        self.price = price
        # self.a += 1

    def __setattr__(self, key, value):
        if type(value) in self.b[key]:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")

# shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.name}, {p.weight}, {p.price}")