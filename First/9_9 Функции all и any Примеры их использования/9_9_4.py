# put your python code here
a=list(map(int,input().split()))
b=all(map(lambda x: x>2,a))
if b:
    print('учится')
else:
    print('отчислен')