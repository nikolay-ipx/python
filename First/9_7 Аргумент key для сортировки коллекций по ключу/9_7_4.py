import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
def sort_tup(list_twodimensionale_2):
    list_template = ['Имя', 'Зачет', 'Оценка', 'Номер']
    list_index = list()
    for x in range(0,4):
        list_index.append(list_twodimensionale_2[0].index(list_template[x]))
    return list_index
list_twodimensionale_2 = tuple(tuple(int(z) if z.isdigit() else z for z in y.split(';')) for y in lst_in)
t_sorted = tuple(tuple(y[z] for z in sort_tup(list_twodimensionale_2)) for y in list_twodimensionale_2)