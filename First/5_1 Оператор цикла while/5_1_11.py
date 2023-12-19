n,m=map(int,input().split())
c=list(range(n+1,m,2))
d=len(c)
e=[]
f=0
while f<d:
    e.append(c[f])
    f+=1
print(*e)