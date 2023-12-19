import sys
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
A=[[row[i] for row in lst_in] for i in range(len(lst_in[0]))]
for row in A:
    print(*row)