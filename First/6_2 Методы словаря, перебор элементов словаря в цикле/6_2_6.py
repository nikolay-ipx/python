import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
a=[]
b={}
for i in lst_in:
    a.append(i.split())
for i in a:
    if i[0] not in b:
        b[i[0]]=[i[1]]
    else:
        b[i[0]].append(i[1])
for x,y in b.items():
    print(str(x)+':',', '.join(y))