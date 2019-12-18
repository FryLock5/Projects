fileName = input(str("Please enter a file name: "))
searchFile = open(fileName, "r")
lineNumber = 0
line = 0
count=0
while True:
    num_lines = sum(1 for line in open(fileName))
    print("The file has", num_lines,"lines.")
    lineNumber = int(input("Please enter a line number[0 to quit]: "))
    if lineNumber==0:
        break
    else:
        for line in open(fileName):
            if count==lineNumber-1:
                print(lineNumber,":",line)
                count=0
                break
            count+=1
