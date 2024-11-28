# put your python code here
from xml.etree.ElementInclude import include


def counter_add():
    def a(x):
        return x+5
    return a
k = int(input())
cnt=counter_add()
print(cnt(k))