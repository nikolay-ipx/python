import sys
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
b=len(lst_in)
for x in range(b):
    for y in range(x):
        if lst_in[x][y] != lst_in[y][x]:
            print('НЕТ')
            break
    else:
        continue
    break
else:
    print('ДА')