import random
random.seed(1)
a=list(map(str,input().split()))
b=random.sample(a,3)
print(*b)