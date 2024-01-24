# ввод значения N (эту переменную не менять)
N = int(input())
def get_sum(N):
    c=[]
    for i in range(1,N+1):
        c.append(i)
        yield sum(c)
# здесь продолжайте программу