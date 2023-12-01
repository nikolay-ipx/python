class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.gd = gd
        self.goods.append(self.gd)

    def remove(self, index):
        self.index = index
        self.goods.pop(self.index)

    def get_list(self):
        return [f'{x.name}: {x.price}' for x in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('samsung', 50000))
cart.add(TV('sony', 70000))
cart.add(Table('стол стеклянный', 10000))
cart.add(Notebook('hp', 40000))
cart.add(Notebook('asus', 40000))