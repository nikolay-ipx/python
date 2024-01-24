# put your python code here
a=sorted(map(str,input().split()),key=len,reverse=True)
print(*a)