import random
from string import ascii_lowercase, ascii_uppercase
random.seed(1)
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
N=int(input())
def gen(N):
    g=[]
    for i in range(N):
        g.append(chars[random.randint(0,len(chars)-1)])
    yield ''.join(g)

s=5
while s!=0:
    for i in gen(N):
        print(i)
    s-=1