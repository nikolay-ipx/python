# put your python code here
a=list(map(int,input().split()))
b=filter(lambda x: len(str(abs(x)))==2 ,a)
for i in b:
    print(i,end=' ')