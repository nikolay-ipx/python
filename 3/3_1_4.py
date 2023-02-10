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
    b = {'name' : (str, ), 'weight' : (float, int), 'price' : (int, float), 'id' : (int, )}
    def __init__(self, name, weight, price):

        self.name = name
        self.weight = weight
        self.price = price
        self.id = self.a
        Product.a += 1

    def __setattr__(self, key, value):
        if type(value) not in self.b[key]:
            raise TypeError("Неверный тип присваиваемых данных.")
        elif (key == 'weight' or key == 'price') and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)


    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 9)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.weight}, {p.price}")
print(book.__dict__)