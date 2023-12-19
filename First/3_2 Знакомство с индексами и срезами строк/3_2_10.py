a,b = map(str,input().split())
c=len(b)
a=a[1:c:2]
b=b[1::2]
print(a==b)