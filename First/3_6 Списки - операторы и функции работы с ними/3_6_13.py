cities = ["Москва", "Тверь", "Вологда"]
lst=list(map(str,input().split()))
lst=lst+cities
print(*lst)