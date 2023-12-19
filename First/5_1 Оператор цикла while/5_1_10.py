a=1000
d=1000
n=int(input())
c=0
while c<n:
    d=d*5/100
    d=d+a
    a=d
    c+=1
print(round(d,2))