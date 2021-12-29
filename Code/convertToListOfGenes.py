
nameInput = input("Enter name of file that needs to be parsed: ")
nameOutput = input("Enter name for file that will store results: ")

fileInput = open(nameInput, 'r')
fileOutput = open(nameOutput, 'w')

for line in fileInput:
    temp = line.split(' ')[1]
    fileOutput.write(temp)
    fileOutput.write("\n")

fileInput.close()
fileOutput.close()