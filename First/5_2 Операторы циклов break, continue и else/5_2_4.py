a=list(map(str,input().split()))
b=0
c=len(a)
while b<c:
    if len(a[b])>5:
        if c==b+1:
            print('ДА')
            break
        b+=1
    else:
        print('НЕТ')
        break