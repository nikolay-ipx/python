class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj
    def remove_obj(self):
        if self.tail is None:
            return
        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)
        self.tail = prev
        if self.tail == None:
            self.head = None
    def get_data(self):
        a = []
        b = self.head
        while b:
            a.append(b.get_data())
            b = b.get_next()
        return a

class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data
    def set_next(self, obj):
        self.__next = obj
    def set_prev(self, obj):
        self.__prev = obj
    def get_next(self):
        return self.__next
    def get_prev(self):
        return self.__prev
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
print(lst.get_data())
lst.remove_obj()
print(lst.get_data())