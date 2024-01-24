import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
b=list(map(int, x.split()) for x in lst_in)
z=zip(*b)
for i in z:
    print(*i)