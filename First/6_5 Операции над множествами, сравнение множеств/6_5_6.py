# put your python code here
a=set(map(str,input().split()))
b=set(map(str,input().split()))
for i in a:
    if i not in b:
        print('НЕТ')
        break
    else:
        continue
else:
    print('ДА')
