a=[x.split('=') for x in input().split()]
d=dict([[a[x][0],int(a[x][1])] for x in range(0,len(a))])
print(*sorted(d.items()))