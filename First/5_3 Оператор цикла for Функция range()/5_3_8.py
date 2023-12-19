n=int(input())
a=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
if len(a)>2:
    print('НЕТ')
else:
    print('ДА')