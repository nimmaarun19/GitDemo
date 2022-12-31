file = open('textfile.txt')

#print(file.read(5)) #read all file content
# print(file.readline()) #read single line
# print(file.readline())


# line = file.readline()
# while line!="":
#     print(line)
#     line=file.readline()

for line in file.readlines():
    print(line)

file.close()

#read the file and store all the lines in list
#reverse the list
#write back all the lines to file
with open('textfile.txt','r') as reader:
    content = reader.readlines()
    reversed(content) #reverse the content
    with open('textfile.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)

    content2 = reader.readlines()
    print(content2)