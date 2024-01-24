def get_list_dig(it):
    s=[]
    for i in it:
        if type(i)==int or type(i)==float:
            s.append(i)
    return s