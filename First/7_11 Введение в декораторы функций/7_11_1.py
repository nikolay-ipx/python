def get_sq(width, height):
    return width*height
def func_show (get_sq):
    def p(*args,**kwargs):
        print( f"Площадь прямоугольника: {get_sq(*args,**kwargs)}")
    return p