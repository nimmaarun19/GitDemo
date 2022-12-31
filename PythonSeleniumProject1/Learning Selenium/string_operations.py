str = "Hello world this is strings.operations"
str1 = "second String"
str2 = "world"
str4 ="$$     ksfds     "

print(str[1]) #fetch character

print(str[0:5]) #substring

print(str +" " + str1) #concatenation

print(str2 in str) #check substring present in main string

var = str.split(".") #split string based on delimter
print(var)

print("This is raw str4 string: " + str4)   #strip white spaces
print("This is Left stripped str4 string: " + str4.lstrip())
print("This is Right stripped str4 string: " + str4.rstrip())
print("This is full stripped str4 string: " + str4.strip())
print("This is $$ stripped str4 string: " + str4.strip("$").strip())






