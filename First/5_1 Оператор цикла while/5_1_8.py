n=int(input())
a=1
b=1
d=0
k=n
s=[1,1]
if n==1:
    print(a)
elif n==2:
    print(a)
else:
    while d<k-2:
        n=a+b
        s.append(n)
        a=b
        b=n
        d+=1
    print(*s)