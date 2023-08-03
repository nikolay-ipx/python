class Goods:
    title = 'Мороженое'
    weight = 154
    tp = 'Еда'
    price = 1024
setattr(Goods, 'price', 2048)
Goods.inflation = 100 # или так