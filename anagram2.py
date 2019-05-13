from anagramHelper import *

# Create the dictionary
testDict = createDictFromList(convertToListFromFile('9dict.txt'))
# Input test string
inputStr = input('[Python3] Enter a 9-letter anagram: ')
# print result
findWordFromDict(inputStr,testDict)