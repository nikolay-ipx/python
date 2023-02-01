class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value is None:
            self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj

        self.last = obj

        if self.top is None:
            self.top = obj

    def pop(self):
        h = self.top
        if h is None:
            return
        while h.next != self.last:
            h = h.next
        if h:
            h.next = None

        last = self.last
        self.last = h
        if self.last is None:
            self.top = None

        return last

    def get_data(self):
        a = []
        b = self.top


        while b:
            a.append(b.data)
            b = b.next

        return a


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()
print(res)
