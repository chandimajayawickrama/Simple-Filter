import sys

# Function to seperate the string into a List of characters
def seperate(string):
    a = list(string)
    return a
    
# Function to take two strings, check whether the string2 has letters of the string1
# Return a boolean whether the two string has same letters
def checkEqual(str1,str2):
    bool = False
	#Seperate each string into a List of characters.
    x = seperate(str1)
    y = seperate(str2)
    i = 0
	#Check whether the letters in each string are the same.
    while i < len(y):
        j = 0
        while j < len(x):
            if  y[i] == x[j]:
                bool = True
                break #Break the loop if the letter matches the given string(as a command line argument)
            else:
                bool = False
            j+=1
        if bool == False:
            break
        i+=1

    return bool

# Function to go through a List of words and return a List of the matching words
def printString(string,aList):
    sample = []
    i = 0
    while i <len(aList):
        if checkEqual(string,aList[i])==True:
            sample.append(aList[i])
        i+=1
    return sample
	
# Function to read a text file and extract the words that match the letters of the given string
def read_file(filename,string):
    lines = []
	#Read a file and check each string and put the valid strings(words)to a List.
    with open(filename) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return printString(string,lines)

print(read_file(sys.argv[1],sys.argv[2]))
