from ooops_demo import Calculator

class Childdemo(Calculator):
    num2 = 200


    def getchildData(self):
        print("I am in in child method")
        return self.num2 + self.firstnumber + self.secondnumber + self.summation()


cobj = Childdemo(3,4)
print(cobj.getchildData())