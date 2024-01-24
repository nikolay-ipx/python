# put your python code here
a=set(map(int,input().split()))
a=sorted(a,reverse=True)
print(*a[:4])