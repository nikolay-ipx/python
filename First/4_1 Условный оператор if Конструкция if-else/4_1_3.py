a,b = map(float,input().split())
if a%b==0:
    print(int(a/b))
else:
    print(f'{int(a)} на {int(b)} нацело не делится')