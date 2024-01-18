import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
a={x for x in lst_in}
print(len(a))