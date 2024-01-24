import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
lst_in=dict((x.split('=')) for x in lst_in)
menu={**menu,**lst_in}