TYPE_OS = 1


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

class Dialog:

    def __new__(cls, *args, **kwargs):
        a=0
        if TYPE_OS == 1:
            a = super().__new__(DialogWindows)
        else:
            a = super().__new__(DialogLinux)
        a.name = args[0]
        return a