import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
b=list(map(int, x.split()) for x in lst_in)
a=list(zip(*zip(*b)))
for i in a:
    print(*i)