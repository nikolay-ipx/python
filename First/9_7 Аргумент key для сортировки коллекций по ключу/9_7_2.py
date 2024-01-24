import sys
def di(s):
    a=sorted(s,reverse=True)
    d=[s[x] for x in a]
    return d
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [x.split('=') for x in lst_in]
lst_in={int(key):value for value,key in lst_in}
print(*di(lst_in))