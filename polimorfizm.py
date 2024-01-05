class Country:
    def __init__(self):
        pass
class Russian(Country):
    def __init__(self, population):
        super().__init__()
        self.population=population
    def setPopulation(self):
        self.population
    def getPopulation(self):
        return self.population
class Canada(Country):
    def __init__(self, population):
        super().__init__()
        self.population=population
    def setPopulation(self):
        self.population
    def getPopulation(self):
        return self.population
class Germany(Country):
    def __init__(self, population):
        super().__init__()
        self.population=population
    def setPopulation(self):
        self.population
    def getPopulation(self):
        return self.population
        






a=Russian(303290300000)
b=Canada(1020032)
c=Germany(2398765432345678)

print(a.getPopulation())
print(b.getPopulation())
print(c.getPopulation())