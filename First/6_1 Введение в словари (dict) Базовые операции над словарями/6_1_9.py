c={}
d=[]
while True:
    b=int(input())
    if b==0:
        break
    else:
        d.append(b)
for i in d:
    if i not in c:
        c[i]=i**0.5
        print(round(c[i],2))
    elif i in c:
        print('значение из кэша:',round(c[i],2))