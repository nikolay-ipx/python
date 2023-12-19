a=100
b=999
c=[]
while a<=b:
    if a%47==43:
        if a%3==0:
            c.append(a)
    a+=1
print(*c)