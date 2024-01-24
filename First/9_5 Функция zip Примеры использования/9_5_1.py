a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=zip(a,b)
d=[]
for i in range(3):
    a, b = next(c)
    d.append(a*b)
print(*d)