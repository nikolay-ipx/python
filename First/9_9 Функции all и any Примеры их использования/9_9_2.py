# put your python code here
a=list(map(float,input().split()))
b=any(map(lambda x: x<0,a))
print(b)