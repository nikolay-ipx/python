# put your python code here
import random
from string import ascii_lowercase, ascii_uppercase
random.seed(1)
chars = ascii_lowercase + ascii_uppercase
N=int(input())
def gen(N):
    g=[]
    for i in range(N):
        g.append(chars[random.randint(0,len(chars)-1)])
    yield ''.join(g)+'@mail.ru'

s=5
while s!=0:
    for i in gen(N):
        print(i)
    s-=1