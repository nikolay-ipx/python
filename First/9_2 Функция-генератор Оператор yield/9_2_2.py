# put your python code here
def get_sum(N):
    x1,x2,x3=1,1,1
    for i in range(3):
        yield 1
    for i in range(4,N+1):
        x1,x2,x3=x2,x3,x1+x2+x3
        yield x3
N=int(input())
for i in get_sum(N):
    print(i,end=' ')