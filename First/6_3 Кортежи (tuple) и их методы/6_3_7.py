a=tuple(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
b=tuple(b)
print(*b)