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
    #check if duplicate
    if  KeyInput in ListOfKeys:
        print("Break")
        break
    ListOfKeys.append(KeyInput)
    #check if spaces
    if " " in KeyInput:
        print("fail")
        break
    TranslationInput = input("Enter the Translation: ")
    myDict[KeyInput] = TranslationInput
#sentence
Sentence = input("Enter a sentence: ")
index = 0
PlzWork = Sentence.split(" ")
for i in range(0, len(PlzWork)):
  word = PlzWork[i]
  if word in myDict:
    PlzWork[i] = myDict[word]
#print(PlzWork)
OutputSentence = " ".join(PlzWork)
print(OutputSentence)
print(myDict)
