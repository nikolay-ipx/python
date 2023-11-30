class Car:
    __model = None
    @property
    def model(self):
        if type(self.__model) is str:
            return self.__model

    @model.setter
    def model(self,model):
        if 2 <= len(model) <= 100:
            self.__model = model


car = Car()
car.model = "Toyota"
print(car.__dict__)