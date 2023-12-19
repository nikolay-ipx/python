nazvanie=input()
avtor=input()
number_sum=int(input())
price=float(input())
book=[nazvanie,avtor,number_sum,price]
del book[2]
book[1]='Пушкин'
book[2]=book[2]*2
print(book)