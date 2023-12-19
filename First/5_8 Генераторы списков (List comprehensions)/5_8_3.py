N=int(input())
a=[[0 for x in range(N)] for x in range(N)]
b=len(a)
for i in range(b):
    for x in range(i+1):
        a[x][x]=1
for i in a:
    print(*i)