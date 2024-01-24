import sys
def di(s):
    a=sorted(s)
    d=[s[x] for x in a]
    return d[:3]
lst_in = list(map(str.strip, sys.stdin.readlines()))
a=[x.split(':') for x in lst_in]
b=dict(a)
b={int(value):key for key,value in b.items()}
print(*di(b))