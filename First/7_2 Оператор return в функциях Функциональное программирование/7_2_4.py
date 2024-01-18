# put your python code here
def is_triangle(a):
    if a%2==0:
        print(a)
a=[]
while True:
    b=int(input())
    if b==1:
        break
    else:
        a.append(b)
for i in a:
    is_triangle(i)