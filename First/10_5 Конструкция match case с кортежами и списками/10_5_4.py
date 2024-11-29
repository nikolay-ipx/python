# fio = ('Сидоров', 'Петр', 'Иванович')
#
# match fio:
#     case f1, f2, f3:
#         res = ", ".join((f2, f3, f1))
#     case _:
#         res = "Некорректный формат данных"
#
# print(res)
#
# size = [100, 200, 50]
#
# match size:
#     case s1, s2:     # 1-й блок case
#         res = ", ".join(map(str, [s2, s1]))
#         print(res)
#     case s1, s2, s3: # 2-й блок case
#         res = ", ".join(map(str, [s2, s3, s1]))
#         print(res)
#     case _:          # 3-й блок case
#         res = "Некорректный формат данных"
#         print(res)
#
# student = [['Троечников С.М.'], [2], 3, 3, 2, 3, 4, 3, 5, 5, 1]
#
# match student:
#     # case fio, m1, m2, m3:               # 1-й case
#     #     print(f"{fio}: {m1} {m2} {m3}")
#     # case tuple() as fio, m1, m2, m3, *_: # 2-й case
#     #     print(f"{fio}: {m1} {m2} {m3}")
#     case list() as fio, m1, *_: # 3-й case
#         print(f"{fio}: {m1}")
#     # case list() as fio, m1, m2, m3, *_:  # 3-й case
#     #     print(f"{fio}: {m1} {m2} {m3}")
#     # case tuple() as fio, m1, m2, m3:    # 4-й case
#     #     print(f"{fio}: {m1} {m2} {m3}")
#     case _:                             # 5-й case
#         print("Некорректный формат данных")

# t = (int, str, str, float, int)
# book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
# match book:
#     case _, avtor, nazvanie if len(book) == 3 :
#         print(f'{avtor}, {nazvanie}')
#     case _, avtor, nazvanie, cena if len(book) == 4:
#         print(f'{avtor}, {nazvanie}, {cena}')
#     case _, avtor, nazvanie, cena, god if len(book) == 5 and cena == 0:
#         print(f'{avtor}, {nazvanie}, {god}')
#     case _, avtor, nazvanie, cena, god if len(book) == 5 and cena != 0:
#         print(f'{avtor}, {nazvanie}, {cena}, {god}')

t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
match book:
    case _, avtor, nazvanie if len(book) == 3 :
        print('Yes')
    case _, avtor, nazvanie, cena if len(book) == 4:
        print('Yes')
    case _, avtor, nazvanie, cena, god if len(book) == 5 and cena == 0:
        print('Yes')
    case _, avtor, nazvanie, cena, god if len(book) == 5 and cena != 0:
        print('Yes')
    case _:
        print('No')