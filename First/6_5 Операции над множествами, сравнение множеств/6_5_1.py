# put your python code here
a=set(map(int,input().split()))
b=set(map(int,input().split()))
s=a&b
print(*sorted(s))