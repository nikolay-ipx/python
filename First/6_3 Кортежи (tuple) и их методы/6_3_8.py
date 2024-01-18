a=tuple(map(int,input().split()))
for x,y in enumerate(a):
    if a.count(y)>=2:
        print(x,end=' ')