import sys
import random
random.seed(1)
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [[int(x) for x in x.split()] for x in lst_in]
a=zip(zip(*lst_in))
b=[]
for i in a:
    for x in i:
        b.append(list(x))
random.shuffle(b)
c=zip(zip(*b))
d=[]
for i in c:
    for x in i:
        d.append(list(x))
for i in d:
    print(*i)