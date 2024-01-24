a=list(map(str,input().split()))
for i in range(int(len(a)/3)):
    b=list(x for x in a[:3])
    a=a[3:]
    print(*b)