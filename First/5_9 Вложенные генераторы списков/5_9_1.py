import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
b=[x
   for i in lst_in[::-1]
   for x in i[::-1]
   ]
print(*b)