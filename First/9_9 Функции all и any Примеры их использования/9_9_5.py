def is_free(lst):
    b=False
    for i in lst:
        b=b or any(map(lambda x: x=='#',i))
    return b