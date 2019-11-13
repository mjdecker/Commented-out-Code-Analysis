import sys
import glob
import os

oFile = open("letterFreq.py", "w")
countCode = 0
countComment = 0
letterFreqString = "import numpy as np\nimport sys\nimport pandas as pd\ndef load_letterFreq() :\n    data = {'data': array("
oFile.write('%s' % (letterFreqString))

keyboardDict = {'a': [0,0], 'b': [0,0], 'c': [0,0], 'd': [0,0], 'e': [0,0], 'f': [0,0], 'g': [0,0], 'h': [0,0],
                'i': [0,0], 'j': [0,0], 'k': [0,0], 'l': [0,0], 'm': [0,0], 'n': [0,0], 'o': [0,0], 'p': [0,0],
                'q': [0,0], 'r': [0,0], 's': [0,0], 't': [0,0], 'u': [0,0], 'v': [0,0], 'w': [0,0], 'x': [0,0],
                'y': [0,0], 'z': [0,0], '!': [0,0], '@': [0,0], '#': [0,0], '$': [0,0], '%': [0,0], '^': [0,0],
                '&': [0,0], '*': [0,0], '(': [0,0], ')': [0,0], '1': [0,0], '2': [0,0], '3': [0,0], '4': [0,0],
                '5': [0,0], '6': [0,0], '7': [0,0], '8': [0,0], '9': [0,0], '0': [0,0], '-': [0,0], '_': [0,0],
                '+': [0,0], '=': [0,0], '{': [0,0], '[': [0,0], '}': [0,0], ']': [0,0], '|': [0,0], '\\': [0,0],
                ':': [0,0], ';': [0,0], '\'': [0,0], '"': [0,0], '<': [0,0], ',': [0,0], '>': [0,0], '.': [0,0],
                '?': [0,0], '/': [0,0], ' ': [0,0], '~': [0,0], '`': [0,0], '\t': [0,0], '\n': [0,0], '\f': [0,0],
                '\r': [0,0], '\b': [0,0], '\v': [0,0], '\0': [0,0], 'unk': [0,0]}

charCount = 0
lineCount = 0
for fileName in glob.glob("Comments.md") :
    inFile = open(fileName, "r")
    for line in inFile :
        countCode += 1
        for i in range (0, line.__len__()) :
            char = line[i:i+1]
            char = char.lower()
            if char in keyboardDict.keys() :
                keyboardDict[char][0] = keyboardDict[char][0] + 1
                charCount = charCount + 1
            else :
                keyboardDict['unk'][0] = keyboardDict['unk'][0] + 1
                charCount = charCount + 1
        oFile.write('[')
        for key in keyboardDict.keys() :
            keyboardDict[key][1] = keyboardDict[key][1] + keyboardDict[key][0]/charCount
            if key != 'unk' :
                oFile.write('%s%s' % ((keyboardDict[key][0]/charCount), ', '))
            else :
                oFile.write('%s' % ((keyboardDict[key][0]/charCount)))
            keyboardDict[key][0] = 0
        lineCount = lineCount + 1
        charCount = 0
        oFile.write('], ')
    for key in keyboardDict.keys() :
        keyboardDict[key][1] = keyboardDict[key][1]/lineCount
    inFile.close()

keyboardDict = {'a': [0,0], 'b': [0,0], 'c': [0,0], 'd': [0,0], 'e': [0,0], 'f': [0,0], 'g': [0,0], 'h': [0,0],
                'i': [0,0], 'j': [0,0], 'k': [0,0], 'l': [0,0], 'm': [0,0], 'n': [0,0], 'o': [0,0], 'p': [0,0],
                'q': [0,0], 'r': [0,0], 's': [0,0], 't': [0,0], 'u': [0,0], 'v': [0,0], 'w': [0,0], 'x': [0,0],
                'y': [0,0], 'z': [0,0], '!': [0,0], '@': [0,0], '#': [0,0], '$': [0,0], '%': [0,0], '^': [0,0],
                '&': [0,0], '*': [0,0], '(': [0,0], ')': [0,0], '1': [0,0], '2': [0,0], '3': [0,0], '4': [0,0],
                '5': [0,0], '6': [0,0], '7': [0,0], '8': [0,0], '9': [0,0], '0': [0,0], '-': [0,0], '_': [0,0],
                '+': [0,0], '=': [0,0], '{': [0,0], '[': [0,0], '}': [0,0], ']': [0,0], '|': [0,0], '\\': [0,0],
                ':': [0,0], ';': [0,0], '\'': [0,0], '"': [0,0], '<': [0,0], ',': [0,0], '>': [0,0], '.': [0,0],
                '?': [0,0], '/': [0,0], ' ': [0,0], '~': [0,0], '`': [0,0], '\t': [0,0], '\n': [0,0], '\f': [0,0],
                '\r': [0,0], '\b': [0,0], '\v': [0,0], '\0': [0,0], 'unk': [0,0]}

charCount = 0
lineCount = 0
for fileName in glob.glob("Code.md"):
    inFileFinal = open(fileName, "r")
    inFile = open(fileName, "r")
    size = os.path.getsize("Code.md")
    sizeFinal = os.path.getsize("Code.md")
    for lineFinal in inFileFinal :
        sizeFinal -= lineFinal.__len__()
    for line in inFile :
        countComment += 1
        size -= line.__len__()
        for i in range (0, line.__len__()) :
            char = line[i:i+1]
            char = char.lower()
            if char in keyboardDict.keys() :
                keyboardDict[char][0] = keyboardDict[char][0] + 1
                charCount = charCount + 1
            else :
                keyboardDict['unk'][0] = keyboardDict['unk'][0] + 1
                charCount = charCount + 1
        oFile.write('[')
        for key in keyboardDict.keys() :
            keyboardDict[key][1] = keyboardDict[key][1] + keyboardDict[key][0]/charCount
            if key != 'unk' :
                oFile.write('%s%s' % ((keyboardDict[key][0]/charCount), ', '))
            else :
                oFile.write('%s' % ((keyboardDict[key][0]/charCount)))
            keyboardDict[key][0] = 0
        lineCount = lineCount + 1
        charCount = 0
        if size == sizeFinal :
            oFile.write('])')
        else :
            oFile.write('], ')
    for key in keyboardDict.keys() :
        keyboardDict[key][1] = keyboardDict[key][1]/lineCount
    inFile.close()
    inFileFinal.close()

print(countCode)
print(countComment)
oFile.write('%s' % (", 'target': array(["))

for i in range(0, countCode) :
    i += 1
    oFile.write('%s' % ("0, "))

for x in range(0, countComment) :
    if x == 499 :
        oFile.write('%s' % ("1"))
    else :
        oFile.write('%s' % ("1, "))
    x += 1

oFile.write('%s' % ("]), 'target_names': array(['Code', 'Comment'], dtype='<U10'), 'DESCR': 'Letter Frequency Database\n====================\n\nNotes\n-----\nData Set Characteristics:\n    :Number of Instances: 1000 (500 in each of two classes)\n    :Number of Attributes: 77 numeric, predictive attributes and the class\n    :Attribute Information:\n        - 77 distinct Ascii charecters all letters are lowercase        - class:\n                - Code\n                - Comment\n    :Summary Statistics:\n\n   ============== ==== ==== ======= ===== ====================\n\n    :Missing Attribute Values: None\n    :Class Distribution: 50% for each of 2 classes.\n    :Creator: B.E. Grills\n    :Date: October, 2019\n\n This data set was built over the course of eight months with the help and advise of Dr. M.J. Decker.\nAll of the data was first verified by hand to ensure that we knew all data was accurate. The comments that were analyzed for this data set were pulled\nfrom 18 different projects written in C, C++, C#, and Java with the help of srcML.\nThe goal of this project is to develop a method to automate the process of detecting commented-out code.\n\n', 'feature_names': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '+', '=', '{', '[', '}', ']', '|', '\\', ':', ';', "'", '"', '<', ',', '>', '.', '?', '/', ' ', '~', '`', '\t', '\n', '\x0c', '\r', '\x08', '\x0b', '\x00', 'unk']}"))
