# put your python code here
def out(a):
    if len(a)<6:
        return False
    else:
        return a
a=input().split()
b=[x for x in a if out(x)!=False]
print(*b)
