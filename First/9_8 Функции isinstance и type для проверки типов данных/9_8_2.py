def get_add(a, b):
    if type(a)==bool or type(b)==bool:
        return None
    elif type(a)==type(b):
        return a+b
    elif isinstance(a,(int,float)) is isinstance(b,(int,float)):
        return a+b
    else:
        return None