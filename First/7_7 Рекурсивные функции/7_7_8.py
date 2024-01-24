# put your python code here
a=list(map(int, input().split()))
def b(a):
    if len(a)>1:
        a1=b(a[:len(a)//2])
        a2=b(a[len(a)//2:])
        return sorted(a1+a2)
    else:
        return a
print(*b(a))