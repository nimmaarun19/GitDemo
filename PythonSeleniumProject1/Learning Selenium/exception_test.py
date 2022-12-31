
itemscart = 0

if itemscart !=2:
    #raise Exception('Products in cart is not equal to two')
    pass

assert(itemscart == 0)

#try, catch method:

try:
    with open('textfiles.txt','r') as reader:
        reader.read()

except:
    print("There is some error in file - PLS CHECK")

try:
    with open('textfiles.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up all resources")