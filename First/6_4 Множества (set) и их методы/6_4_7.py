import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in=[x.split(':') for x in lst_in]
a={x[0][0] for x in lst_in}
print(len(a))