
class Calculator:
    num = 50
    def __init__(self):
        print("testing the constructor")

    #The below is called a method. You can not call a method inside a class. You must call the method
    #outside of the class
    def getData(self):
        print("I am now executing a method in class")

#On the left is the variable. The vairable  is assigned to the object, which is after the equals sign
#By calling the object with Calculator() we call the testing the constructor print
Object = Calculator()

#To call the method within the class, you now use the object followed by a dot, and then call the method
#The object is case sensitive

Object.getData()

#I can also call the variable within the Class too. See below:
print(Object.num)