# put your python code here
a, b = map(int, input().split())
c=(abs(x) for x in range(a,b))
d=0
for i in c:
    if d <5:
        d += 1
        print(i)
    else:
        break