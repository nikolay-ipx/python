import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
g = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник']
a=[x.split('=') for x in lst_in]
def get(x):
    if x[1] in g:
        return g.index(x[1])
lst = sorted(a, key=get)