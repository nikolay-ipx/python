class LessonItem:
    a = {'title' : str, 'practices' : int, 'duration' : int}
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if type(value) is not self.a[key]:
            raise TypeError("Неверный тип присваиваемых данных.")
        elif (key == 'practices' or key == 'duration') and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in (self.title, self.practices, self.duration):
            return


c=LessonItem('2',1,3)
del c.title
print(c.__dict__)