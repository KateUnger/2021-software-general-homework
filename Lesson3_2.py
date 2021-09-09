print("Welcome to the dictionary program!")
myDict = {}
KeyInput = ""
TranslationInput = ""
ListOfKeys = []
while True:
    KeyInput = input("Enter a word or hit enter to end: ")
    #check if empty
    if KeyInput == "":
        break
    TranslationInput = input("Enter the Translation: ")
    myDict[KeyInput] = TranslationInput
print(myDict)