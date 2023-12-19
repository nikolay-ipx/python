# put your python code here
a=True
b=0
while a:
    c=int(input())
    if c==0:
        a=False
    elif c<0:
        continue
    elif b==0:
        b+=c
    else:
        b=b*c
print(b)