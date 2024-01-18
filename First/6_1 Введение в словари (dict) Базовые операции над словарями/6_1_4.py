import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
d=[x.split('=') for x in lst_in]
print(d)
d=dict([[int(d[x][0]),d[x][1]] for x in range(0,len(d))])
print(*sorted(d.items()))