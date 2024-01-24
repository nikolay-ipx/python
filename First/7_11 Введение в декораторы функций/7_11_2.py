def show_menu(fun):
    def str(args):
        for x,y in enumerate(fun(args)):
            print(f'{x+1}. {y}')
    return str
@show_menu
def get_menu(s):
    return s.split()