import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst2D=[[int(x) for x in x.split()] for x in lst_in]