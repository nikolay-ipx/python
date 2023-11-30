class Translator :
    def add(self, eng, rus):
        if 'translator' not in self.__dict__:
            self.translator={}
        self.translator.setdefault(eng,[])
        if rus not in self.translator[eng]:
            self.translator[eng].append(rus)

    def remove(self, eng):
        self.translator.pop(eng,False)

    def translate(self, eng):
        return(self.translator[eng])
    
tr =Translator()
tr.add('tree','дерево')
tr.add('car','машина')
tr.add('car','автомобиль')
tr.add('leaf','лист')
tr.add('river','река')
tr.add('go','идти')
tr.add('go','ехать')
tr.add('go','ходить')
tr.add('milk','молоко')
tr.remove('car')
print(*tr.translate('go'))