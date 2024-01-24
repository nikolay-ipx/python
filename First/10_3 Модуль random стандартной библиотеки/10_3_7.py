import random


def verify(a):
    for x, y in enumerate(a):
        for i, o in enumerate(y):
            if o == 1:
                p = is_isolate(x, i, a)
                if p == False:
                    return False
                else:
                    continue
    else:
        return True


def is_isolate(a, b, N):
    if a == len(N) - 1 and b != len(N) - 1:
        if N[a][b + 1] == 1:
            return False
    elif b == 0:
        if N[a][b + 1] == 1 or N[a + 1][b] == 1 or N[a + 1][b + 1] == 1:
            return False
    elif 0 < b <= len(N) - 2:
        if N[a][b + 1] == 1 or N[a + 1][b - 1] == 1 or N[a + 1][b] == 1 or N[a + 1][b + 1] == 1:
            return False
    elif b == len(N) - 1 and a != len(N) - 1:
        if N[a + 1][b - 1] == 1 or N[a + 1][b] == 1:
            return False


N = int(input())
P = [[0] * N for i in range(N)]
M = 0
while M < 10:

    r = random.randint(0, N - 1)
    p = random.randint(0, N - 1)

    if P[r][p] == 0:
        P[r][p] = 1
        if verify(P) == True:
            M += 1
            continue
        else:
            P[r][p] = 0