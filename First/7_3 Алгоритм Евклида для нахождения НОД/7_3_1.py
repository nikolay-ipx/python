def get_nod(a,b):
    if b>a:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a