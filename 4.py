class Factory:
    def build_sequence(self):
        self.a = []
        return self.a
    def build_number(self, string):
        self.string = float(string)
        return self.string

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())
print(res)