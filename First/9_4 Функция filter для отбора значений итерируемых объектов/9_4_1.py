# put your python code here
a=list(map(str,input().split()))
b=filter(lambda x: len(x)>5,a)
print(next(b),end=' ')
print(next(b),end=' ')
print(next(b))