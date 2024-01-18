a=[x for x in input().lower().split()]
if 'и' not in a:
    print('0')
else:
    b={x: a.count(x) for x in a}
    print(b['и'])