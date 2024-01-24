def get_data_fig(*N,**kwargs):
    l=[sum(N)]
    if 'type' in kwargs:
        l.append(kwargs['type'])
    if 'color' in kwargs:
        l.append(kwargs['color'])
    if 'closed' in kwargs:
        l.append(kwargs['closed'])
    if 'width' in kwargs:
        l.append(kwargs['width'])
    return l