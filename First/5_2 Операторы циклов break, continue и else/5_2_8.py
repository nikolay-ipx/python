x=int(input())
a=10
b=10
d=1
while a<x:
    a=a*10/100
    b=b+a
    a=b
    d+=1
print(d)