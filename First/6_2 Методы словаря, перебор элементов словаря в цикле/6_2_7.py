a=int(input())*1000
things = {'карандаш': 20, 'зеркальце': 100,
          'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200,
          'молоток': 600, 'пила': 400,
          'удочка': 1200, 'расческа': 40,
          'котелок': 820, 'палатка': 5240,
          'брезент': 2130, 'спички': 10}
b=[]
c=[]
for x,y in things.items():
    b.append(int(y))
b.sort()
b.reverse()
for i in b:
    if a-i>=0:
        a=a-i
        c.append(i)
for i in c:
    for x,y in things.items():
        if y==i:
            print(x,end=' ')