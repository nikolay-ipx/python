import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
for i,a in enumerate(lst_in):
    while a.count('  '):
        a=a.replace('  ',' ')
    while a.count(' '):
        a=a.replace(' ','-')
    lst_in[i]=a
for i in lst_in:
    print(i)