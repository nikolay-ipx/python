# ввод числа n
n = int(input())

# здесь задается функция fact_rec  (переменную n не менять!)
def fact_rec(n):
    if n<=0:
        return 1
    else:
        return n*fact_rec(n-1)