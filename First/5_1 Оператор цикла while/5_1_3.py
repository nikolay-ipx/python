x=float(input())
a=2
b=[]
while a<11:
    c=(a*x)
    c=round(c,1)
    b.append(c)
    a+=1
print(*b)