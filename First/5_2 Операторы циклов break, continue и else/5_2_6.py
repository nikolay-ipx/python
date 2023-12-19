n=int(input())
a=1
b=100
c=[]
while a<=n:
    if n>=b:
        print('слишком большое значение n')
        break
    if a%3==0:
        if a%5==0:
            c.append(a)
    a+=1
else:
    print(*c)