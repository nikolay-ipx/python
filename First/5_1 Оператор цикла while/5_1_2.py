n,m=map(int,input().split())
c=list(range(n,m+1))
d=0
e=[]
while d<len(c):
    e.append(c[d]**2)
    d+=1
print(*e)