import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
a=[]
c=0
while c<len(lst_in):
    if lst_in[c].find(' ') !=-1:
        c+=1
        continue
    else:
        a.append(lst_in[c])
        c+=1
print(*a)