cities = ["Москва", "Тверь", "Вологда"]
lst=list(map(str,input().split()))
lst=cities+lst
print(*lst)