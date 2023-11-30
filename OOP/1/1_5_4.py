from random import randint
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

elements=[(Line,Rect,Ellipse)[randint(0,2)]
          (randint(0,10),randint(0,10),randint(0,10),randint(0,10)) for m in range(217)]
for i in elements:
    if isinstance(i,Line):
        i.sp=(0,0)
        i.ep=(0,0)

for i in elements:
    print(i.__class__.__name__, i.__dict__)