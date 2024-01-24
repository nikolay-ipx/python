import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

a=list(map(int,input().split()))
c=random.uniform(a[0],a[1])
print(round(c,2))