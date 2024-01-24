from functools import wraps
def dec(fun):
    @wraps(fun)
    def dec1(listt):
        a=sum(fun(listt))
        return a
    return dec1
@dec
def get_list (y):
    '''Функция для формирования списка целых значений'''
    a=[int(x) for x in y.split()]
    return a