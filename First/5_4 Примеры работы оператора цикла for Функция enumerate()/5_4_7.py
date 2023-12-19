a=list(map(float,input().split()))
b=0
for i in a:
    if i < 0:
        a.pop(b)
        a.insert(b,-1.0)
    b+=1
print(*a)