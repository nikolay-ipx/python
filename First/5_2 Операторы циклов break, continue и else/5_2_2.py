p = [0] * 10
b = True

while b:
    a = int(input())
    if sum(p) == 5:
        b = False

    elif p[a] == 1:
        continue

    elif p[a] == 0:
        p[a] = 1
        if sum(p) == 5:
            b = False
print(*p)