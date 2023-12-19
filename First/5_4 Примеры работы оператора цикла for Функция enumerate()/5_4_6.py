a=list(map(float,input().split()))
b=[a[0]]
c=0
for i in a:
    if i < b[0]:
        b.clear()
        b.append(i)
print(*b)