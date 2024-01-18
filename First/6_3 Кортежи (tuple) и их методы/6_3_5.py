a=tuple(map(str,input().split()))
b=[]
if 'Ульяновск' in a:
    for x in a:
        if x =='Ульяновск':
            continue
        else:
            b.append(x)
    else:
        b=tuple(b)
        print(*b)
else:
    print(*a)