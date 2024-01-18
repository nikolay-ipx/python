import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
c={}
for x,y in enumerate(lst_in):
    if y not in c.values():
        c[x]=y
        print('HTML-страница для адреса',c[x])
    else:
        for i in c.values():
            if i== y:
                print('Взято из кэша: HTML-страница для адреса',i)