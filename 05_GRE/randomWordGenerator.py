import random

def generateWord(wordArr):
    print(len(wordArr))
    shouldExit = True
    while shouldExit:
        y = input("--------------- Press y to exit ------------------ ")
        if (y.lower() == "y"):
            shouldExit = False
        else:
            randomNumber = random.randint(0, len(wordArr)-1)
            print(wordArr[randomNumber])
