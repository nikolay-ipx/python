# put your python code here
def is_triangle(a):
    if a%2!=0:
        return a
    else:
        pass
a=list(map(int,input().split()))
lst=[x for x in a if is_triangle(x)!=None ]
print(*lst)