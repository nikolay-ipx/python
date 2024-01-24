import sys
def aa(x):
    if int(x[1])>500:
        return x
lst_in = list(map(str.strip, sys.stdin.readlines()))
a=tuple(tuple(x.split('=')) for x in lst_in)

b=filter(aa,a)
for i in b:
    print(i[0],end=' ')