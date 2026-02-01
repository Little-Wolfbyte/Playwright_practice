
class Calculator:
    num = 50

    #The below is called a method. You can not call a method inside a class. You must call the method
    #outside of the class
    def getData(self):
        print("I am now executing a method in class")

#On the left is the variable. The vairable  is assigned to the object, which is after the equals sign
Object = Calculator()

#To call the method within the class, you now use the object followed by a dot, and then call the method
#The object is case sensitive

Object.getData()

#I can also call the variable within the Class too. See below:
print(Object.num)