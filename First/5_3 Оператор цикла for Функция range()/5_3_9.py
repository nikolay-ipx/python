n = input().lower().split()
a = []
b = 1
for i in n:
    a.append(i.strip('ъьы'))
for i in a[:-1]:

    if i[-1] == a[b][0]:
        b += 1
        if b == len(a):
            print('ДА')
        continue
    elif i[-1] != a[b][0]:
        print('НЕТ')
        break