t=('Москва',)
a=tuple(map(str,input().split()))
if t[0] not in a:
    a+=t
    print(*a)
else:
    print(*a)