# put your python code here
a=sorted(map(int,input().split()))
b=sorted(map(int,input().split()),reverse=True)
c=zip(a,b)
d=[]
for i in range(len(max(a,b))):
    a,b=next(c)
    d.append(a+b)
print(*d)