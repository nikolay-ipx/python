# put your python code here
def out(a):
    return (a,len(a))
b=input().split()
d={out(x)[0]:out(x)[1] for x in b}
a = sorted(d, key=lambda x: d[x])
print(*a)