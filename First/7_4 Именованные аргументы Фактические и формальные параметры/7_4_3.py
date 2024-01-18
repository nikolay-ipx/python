def check_password(a,chars='$%!?@#'):
    if len(a)<8:
        return False
    else:
        for i in chars:
            if i in a:
                return True
        else:
            return False
