N=int(input())
a=[[0 for x in range(N)] for x in range(N)]
b=len(a)
c=0
for i in range(b):
    for x in range(b):
        a[i][x]=c
    else:
        c+=1
for i in a:
    print(*i)