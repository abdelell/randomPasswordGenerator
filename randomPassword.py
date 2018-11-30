import random
import string
def randomPasswordGenerator():
    password = ""
    symbols = "-|@.,?/!~#%^&*(){}[]\=*"
    choices = string.ascii_letters + symbols + "1234567890"
    randomLength = random.randrange(10,25)

    for i in range(randomLength):
        randomChar = random.randrange(len(choices))
        password+=choices[randomChar]

    containsUppercase = False
    containsLowercase = False
    containsSymbols = False
    containsNumber = False

    #checks if the requirements are met
    for letter in password:
        if letter.isupper():
            containsUppercase = True
        if letter.islower():
            containsLowercase = True
        if letter.isnumeric():
            containsNumber = True
        for sym in symbols:
            if letter == sym:
                containsSymbols = True
    # if password does not meet the requirements then callse the function again
    if containsUppercase and containsLowercase and containsSymbols and containsNumber:
        print("Number of characters in password are: ", len(password))
        print(password)
    else :
        print("Had to make another password")
        randomPasswordGenerator()
randomPasswordGenerator()
