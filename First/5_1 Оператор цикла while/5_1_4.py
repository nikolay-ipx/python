n=int(input())
a=list(range(1,n+1))
b=len(a)
c=0
d=[]
while c<b:
    d.append(1/a[c])
    c+=1
d=sum(d)
print(round(d,3))