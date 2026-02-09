file = open('test.txt')
#read contents of file
#print(file.read())
line = file.readline()

while line != "":
    print(line)
    line = file.readline()

file.close()