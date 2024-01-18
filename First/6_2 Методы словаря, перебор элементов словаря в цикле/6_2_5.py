a=list(map(int,input().split()))
b={}
for i in a:
    b[i]=i
print(*b.keys())