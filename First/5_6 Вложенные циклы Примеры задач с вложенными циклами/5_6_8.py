a=int(input())
b=[64,32,16,8,4,2,1]
c=0
d=[]
while a!=0:
    if a >= b[c]:
        a = a - b[c]
        d.append(b[c])
    else:
        c+=1
print(*d)