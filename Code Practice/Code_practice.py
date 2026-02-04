
class Calculator:
    num = 50
    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b

    #The below is called a method. You can not call a method inside a class. You must call the method
    #outside of the class
    def getData(self):
        print("I am now executing a method in class")

    def Summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num


#On the left is the variable. The vairable  is assigned to the object, which is after the equals sign
#By calling the object with Calculator() we call the testing the constructor print
Object = Calculator(2,3)

#To call the method within the class, you now use the object followed by a dot, and then call the method
#The object is case sensitive

Object.getData()
print(Object.Summation())

#I can also call the variable within the Class too. See below:
print(Object.num)