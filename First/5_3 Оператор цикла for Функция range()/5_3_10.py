n=int(input())
a=[]
for i in range(0,n):
    if i%3==0 or i%5==0:
        a.append(i)
print(sum(a))