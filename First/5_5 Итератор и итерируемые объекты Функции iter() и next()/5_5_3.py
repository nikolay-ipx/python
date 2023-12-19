a=iter(input())
b=[]
for i in a:
    if i ==' ':
        break
    b.append(i)
b=','.join(b)
b=b.replace(',','')
print(b)