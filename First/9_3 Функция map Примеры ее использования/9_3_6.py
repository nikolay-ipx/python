# put your python code here
a=list(map(lambda x: '-' if len(x) <5  else x,input().split()))
print(*a)