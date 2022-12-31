from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome(executable_path="C:\\BrowserDrivers\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\BrowserDrivers\\geckodriver.exe")
# driver = webdriver.Edge(executable_path="C:\\BrowserDrivers\\msedgedriver.exe")

# driver.get("https://www.rcvacademy.com")
# driver.maximize_window()
# print("The Title is:", driver.title)
# print("{} {}".format("The Title name is : ", driver.title))
# driver.close()

values = [1 , 2 , "Arun Ramesha" , 3, 5]
print(values[0])
print(values[-1])
print(values[2])
print(values[0:4])
values.insert(2,"He is:")
print(values.reverse())
print(values)
del values[1]
print(values)

dic = {"key1":1, "key2":2, "key3":"Hello", "key4":"World"}
dic["Key5"] = "Dictionary"
print(dic)

dic2 = {}
dic2["Key1"] = "Arun"
dic2["Key2"] = "Ramesha"
print(dic2)

greeting = "Good Morning"

if greeting == "Good Morning":
    print("Greeting is correct")
else:
    print("Greeting is not correct")

#for Loop illustation
print("For loop illustration through list")
obj = [1,2,3,4,5,6]
for i in obj:
    print(i*2)

#sum of five natural numbers:
print("For loop illustration through numbers")
sum=0
for j in range(1,6):
    sum=sum+j
print(sum)

#looping through values with skipping every second number
print("looping through values with skipping every second number")
for k in range(1,10,2):
    print(k)

#looping through values with skipping first index
print("looping through values with skipping first index")
for m in range(10):
    print(m)

print("checking for While Loop:")
it=5
while it > 1:
    if it !=3:
        print(it)
    it = it-1

print("checking for While Loop - Continue:")
its=10
while its > 1:
    if its == 8:
        its = its - 1
        continue
    if its == 2:
        break
    print(its)
    its = its-1

print("Started learning Functions:")
def first_function():
    print("This is printing from simple function call:")

first_function()

def second_function(a,b):
    print("Printing from parameterised fucntion: " + a+b)
    
second_function("Arun ", "Ramesha")