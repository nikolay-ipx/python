a=list(map(int, input().split()))
b=list(map(int, input().split()))
n=[a[n]+b[n] for n in range(len(a))]
print(*n)