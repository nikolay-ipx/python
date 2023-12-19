n = int(input())
a = list(range(3, n, 2))
b = a
c = [2]
for i in a:

    for x in b:
        if i / x in b:
            break
        if i / x != 1:
            continue
        c.append(x)
print(*c)