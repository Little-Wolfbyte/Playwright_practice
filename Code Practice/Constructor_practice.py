from Code_practice import Calculator

class Childimp(Calculator):
    num2 = 150

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

Objective = Childimp()
print(Objective.getCompleteData())
