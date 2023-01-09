class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x,self.y)

pt=Point(3,4)
print(pt)
pt2=pt.clone()
print(pt2)
print(pt.con())
print(pt.con())


