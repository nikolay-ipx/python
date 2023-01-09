TYPE_OS = 1


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

class Dialog:

    def __new__(cls, *args, **kwargs):
        a=0
        if TYPE_OS == 1:
            a
        else:
            a = super().__new__(DialogLinux)
        a.name = args[0]
        return a
    def connect(self):
        print(self.name)
# TYPE_OS = 4
a=Dialog('sdf')
print(a.name)


