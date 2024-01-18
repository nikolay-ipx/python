d=input().split(' ')
d=dict([x.split('=') for x in d])
if 'False' in d :
    del d['False']
if '3' in d:
    del d['3']
print(*sorted(d.items()))