# put your python code here
def out(a):
    print(f'Min = {min(a)}, max = {max(a)}, sum = {sum(a)}')
b=list(map(int,input().split()))
out(b)