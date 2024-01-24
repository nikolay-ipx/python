# put your python code here
def dec(start=5):
    def a(fun):
        def b(*args):
            d=fun(*args)+start
            return d
        return b
    return a
@dec(start=5)
def summa(s):
    s=[int(x) for x in s.split()]
    return sum(s)
s=input()
print(summa(s))