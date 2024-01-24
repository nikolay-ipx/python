# put your python code here
def dec(tag='h1'):
    def a(fun):
        def b(*args):
            d=f'<{tag}>{fun(*args)}</{tag}>'
            return d
        return b
    return a
@dec(tag='div')
def summa(s):
    s=s.lower()
    return s
s=input()
print(summa(s))