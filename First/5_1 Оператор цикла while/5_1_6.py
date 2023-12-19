a=input().strip()
b=len(a)
c=1
while c<b:
    a=a.replace('--','-')
    c+=1
print(a)