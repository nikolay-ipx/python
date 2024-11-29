t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
match book:
    case _, avtor, nazvanie if len(book) == 3 and len(avtor) >= 6 and len(nazvanie) >= 10:
        print('Yes')
    case _, avtor, nazvanie, cena if len(book) == 4 and len(avtor) >= 6 and cena >= 0:
        print('Yes')
    case _, avtor, nazvanie, cena, god if len(book) == 5 and cena == 0 and god >= 2020:
        print('Yes')
    case _, avtor, nazvanie, cena, god if len(book) == 5 and cena != 0 and cena >= 0 and god >= 2020:
        print('Yes')
    case _:
        print('No')