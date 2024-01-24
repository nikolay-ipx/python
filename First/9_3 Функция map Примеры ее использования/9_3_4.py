# ввод строки (переменную s не менять)
s = input()
s_lst = s.split()

# здесь продолжайте программу

tp=tuple(tuple(x.split('=')) for x in s_lst)