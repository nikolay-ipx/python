a=list(map(str,input().split()))
b=0
c=len(a)

while b<c:
    if str.lower(a[b][0])==str.lower(a[b][-1]):
        print('ДА')
        break
    elif b+1!=c:
        b+=1
    else:
        print('НЕТ')
        break