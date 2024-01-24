# put your python code here
a=int(input())
b=(x for x in range(-a,a))
c=(abs(x**3) for x in b)
d=0
for i in c:
    if d<4:
        d+=1
        print(i,end=' ')
    else:
        break