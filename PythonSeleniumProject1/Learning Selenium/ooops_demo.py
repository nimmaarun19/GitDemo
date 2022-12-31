class Calculator:
    num = 100

    def __init__(self,a,b):
        print("I am in Constructor")
        self.firstnumber = a
        self.secondnumber = b

    def getData(self):
        print("I am executing from method from class")

    def summation(self):
        return self.firstnumber + self.secondnumber +self.num


obj1 = Calculator(2,3)
obj1.getData()
print(obj1.num)
print(obj1.summation())

obj2 = Calculator(5,10)
obj2.getData()
print(obj2.summation())