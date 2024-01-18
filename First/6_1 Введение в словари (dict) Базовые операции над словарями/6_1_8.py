import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in=[x.split() for x in lst_in]
d={}
for i in lst_in:
    if i[1] not in d:
        d[i[1]]=[i[0]]
    else:
        d[i[1]].append(i[0])
print(*sorted(d.items()))