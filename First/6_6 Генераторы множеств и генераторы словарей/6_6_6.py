import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
a=[x.split(': ') for x in lst_in]
d={}
for i in a:
    if i[0] not in d:
        d[i[0]]={i[1]}
    else:
        d[i[0]].add(i[1])