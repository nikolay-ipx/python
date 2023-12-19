a=list(map(int,input().split()))
b=[]
for i in a:
    c=abs(i)**2
    b.append(c)
print(*b)
