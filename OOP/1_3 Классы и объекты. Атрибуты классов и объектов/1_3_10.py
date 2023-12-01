class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'
p1 = Person()
p1.job1 = 'Программист'
print(p1.__dict__)
print(hasattr(p1,'job1'))