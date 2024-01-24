def get_even_sum(it):
    s=0
    for i in it:
        if type(i)==int and i%2==0:
            s+=i
    return s