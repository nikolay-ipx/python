lst = list(map(str,input().split()))
a=lst[0]!=lst[-1]
lst.append(a)
print(*lst)