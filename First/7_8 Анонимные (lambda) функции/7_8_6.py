def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

# здесь продолжайте программу
a=list(map(int,input().split()))
print(*filter_lst(a))
b=lambda x: x<0
print(*filter_lst(a,b))
c=lambda x: x>=0
print(*filter_lst(a,c))
d=lambda x: 3<=x<=5
print(*filter_lst(a,d))