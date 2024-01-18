# put your python code here
s=set(map(str.lower,input()))
a=[]
for i in s:
    if i.isdigit():
        a.append(i)
if len(a)==0:
    print('НЕТ')
else:
    print(*sorted(a))