t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
def dec(chars = ' !?'):
    def a(fun):
        def b(args):
            d=fun(args)
            for i in chars:
                d=d.replace(i,'-')
            while '--' in d:
                d=d.replace('--','-')
            return d
        return b
    return a
@dec(chars = ' !?')
def summa(s):
    s=s.lower()
    b=[]
    for i in s:
        if i in t:
            b.append(t[i])
        else:
            b.append(i)
    b=''.join(b)
    return b
s=input()
print(summa(s))