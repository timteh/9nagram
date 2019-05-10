# -------------------------------------------------
#   __ _ _ __   __ _  __ _ _ __ __ _ _ __ ___
#  / _` | '_ \ / _` |/ _` | '__/ _` | '_ ` _ \
# | (_| | | | | (_| | (_| | | | (_| | | | | | |
#  \__,_|_| |_|\__,_|\__, |_|  \__,_|_| |_| |_|
#                    |___/
#                 Based on Python 3
# -------------------------------------------------
# 2019-05-10 initial revision

# -------------------------------------------------
#              Convert file to a list
# -------------------------------------------------
def convertToListFromFile(filePath):
    # convert each line to an element in list
    result = list()
    f = open(filePath,'r')
    for line in f:
        result.append(line)
    f.close()
    return result
# -------------------------------------------------
#              Sort Letters in a word
#        e.g.  Singapore -> aeginoprs
#               Shanghai -> aaghhins
# -------------------------------------------------
def sortLetters(strWord):
    # convert to lower case before sorting
    strWord = strWord.lower()
    finalStr = str()
    strWord = list(strWord)
    strWord.sort()
    for item in strWord:
        finalStr = finalStr + item
    return finalStr
# -------------------------------------------------
#      Create a dictionary with sorted letters
#      e.g. microsoft -> cfimoorst [key]
#               apple -> aelpp     [key]
# -------------------------------------------------
def createDictFromList(wordList):
    result = dict()
    for word in wordList:
        # eliminate \n
        word = word.strip()
        # Let sorted letters be the key
        result[sortLetters(word)] = word
    #print (result)
    return result
# -------------------------------------------------
#                 Find word in dict
# -------------------------------------------------
def findWordFromDict(strWord,anagramDict):
    strWord = sortLetters(strWord)
    return anagramDict.get(strWord)