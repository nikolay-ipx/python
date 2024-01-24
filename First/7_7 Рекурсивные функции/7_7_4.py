# ввод числа N
N = int(input())

# здесь задается функция fib_rec (переменную N не менять!)

def fib_rec(N,f = [1,1]):
    if len(f)<N:
        f.append(f[-2]+f[-1])
        fib_rec(N)
    return f