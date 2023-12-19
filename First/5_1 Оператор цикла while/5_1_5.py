a=[]
c=True
while c:
    b=int(input())
    a.append(b)
    if b==0:
        c=False
print(sum(a))