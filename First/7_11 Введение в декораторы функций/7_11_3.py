def show_menu(fun):
    def str(args):
        lst = sorted(fun(args))
        print(*lst)
    return str
@show_menu
def get_list(s):
    return [int(x) for x in s.split()]
s=input()
get_list(s)