lst=list(map(int,input().split()))
a=lst.pop(-1)
lst.append(a%2!=0)
print(*lst)