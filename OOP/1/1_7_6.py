
class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

class Factory:
    @staticmethod
    def build_sequence():
        a=list()
        return a
    @staticmethod
    def build_number(string):
        string=int(string)
        return string

res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
print(res)