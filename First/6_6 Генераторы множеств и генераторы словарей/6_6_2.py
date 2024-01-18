a=input().split()
b={x: y for x,y in enumerate(a[1:],int(a[0]))}
print(b[4])