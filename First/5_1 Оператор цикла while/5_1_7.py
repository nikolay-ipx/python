a=list(map(int,input()))
b=len(a)
c=1
d=1
while c-1<b:
    d=d*a[c-1]
    c+=1
print(d)