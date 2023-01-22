class Clock:
    def __init__(self,x):
        if self.__check_time(x):
            self.__time = x
        else:
            self.__time = 0

    def set_time(self,tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    def __check_time(self, tm):
        return type(tm) == int and 100000 > tm >= 0

clock = Clock(4530)

