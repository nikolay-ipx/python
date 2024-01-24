t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
def dec1(fun):
    def cv (args):
        c=fun(args)
        while '--' in c:
            c=c.replace("--", "-")
        return c
    return cv
@dec1
def b(a):
    c=[]
    for i in a:
        if i in t:
            c.append(t[i])
        if i == ':;.,_' or i == ' ':
            c.append('-')
        elif i not in t:
            c.append(i)
    return ''.join(c)
s=input().lower()
print(b(s))