a, b = map(int, input().split())

x = (0.5 * pow(x/100, 2) - 2.0 for x in range(a*100, b*100))

for i in range(20):
    print(round(next(x), 2), end=' ')