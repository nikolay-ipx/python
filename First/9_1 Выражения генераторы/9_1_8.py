# put your python code here

cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
a=20
while a!=0:
    for i in cities:
        if a==0:
            break
        else:
            print(i,end=' ')
            a-=1