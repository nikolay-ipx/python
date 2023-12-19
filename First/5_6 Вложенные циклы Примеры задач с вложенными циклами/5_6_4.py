import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
a = []
for i in lst_in:
    for x in i:
        a.append(x)
c = 0
l = [0, 5, 10, 15]
s = [1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17, 18]
p = [4, 9, 14, 19]
while c < 20:
    if c in l:
        if a[c] == 1 and (a[c + 1] == 1 or a[c + 5] == 1 or a[c + 6] == 1):
            print('НЕТ')
            break
        elif c == 19:
            print('ДА')
    elif c in s:
        if a[c] == 1 and (a[c + 1] == 1 or a[c + 5] == 1 or a[c + 6] == 1 or a[c + 4] == 1):
            print('НЕТ')
            break
        elif c == 19:
            print('ДА')
    elif c in p:
        if a[c] == 1 and (a[c + 4] == 1 or a[c + 5] == 1):
            print('НЕТ')
            break
        elif c == 19:
            print('ДА')
    c += 1
