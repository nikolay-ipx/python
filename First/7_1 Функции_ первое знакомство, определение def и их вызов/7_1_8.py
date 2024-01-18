def out(a):
    if 'a'<=a<='z' or 'A'<=a<='Z' or '0'<=a<='9' or '_' in a:
        if '@' in a and '.' in a:
            print('ДА')
        else:
            print('НЕТ')
    else:
        print('НЕТ')
a=input()
out(a)