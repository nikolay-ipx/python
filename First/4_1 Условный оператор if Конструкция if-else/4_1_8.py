a,b,c,d=map(int,input().split())
c,d=max(c,d),min(c,d)
if a>c+1 and b>d+1:
    print('ДА')
else:
    print('НЕТ')