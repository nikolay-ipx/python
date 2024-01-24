import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
a=list(map(str,input().split()))
c=random.choice(a)
print(c)
# здесь продолжайте программу