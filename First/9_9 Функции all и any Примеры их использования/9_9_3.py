def is_string(lst):
    a=all(map(lambda x:type(x)==str,lst))
    return a