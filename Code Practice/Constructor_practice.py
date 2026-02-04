from Code_practice import Calculator

class childimp(Calculator):
    num2 = 150

    def __init__(self,a,b):
        Calculator.__init__(self,2,1)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj = childimp()
print(obj.getCompleteData())
