import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
b=[x.split() for x in lst_in]
menu=(tuple(tuple(x) for x in b))
print(menu)