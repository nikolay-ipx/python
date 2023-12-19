a=list(map(int,input()))
if sum(a[0:3]) == sum(a[3:]):
    print('ДА')
else:
    print('НЕТ')