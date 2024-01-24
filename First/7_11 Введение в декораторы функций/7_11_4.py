d = {}
def l_d(fun):
    def dd(a,b):
        for i,j in zip(a.split(),b.split()):
            if i == ' ' or j == ' ':
                continue
            else:
                d[i]=j
                continue
            return d
    return dd

@l_d
def st_list(a,b):
    a = [x for x in a.split()]
    b = [x for x in b.split()]
    return a,b
a=input()
b=input()
st_list(a,b)
print(*sorted(d.items()))