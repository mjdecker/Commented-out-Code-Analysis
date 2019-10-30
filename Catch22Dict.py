import sys
import glob

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
oFile = open('DictComments.py', 'w')
oFile2 = open('DictCommentsLine.py', 'w')
for fileName in glob.glob("E:/school/ThesisProject/v.3/Comments.md") :
    inFile = open(fileName, "r")
    for line in inFile :
        for i in range (0, line.__len__()) :
            char = line[i:i+1]
            char = char.lower()
            if char in keyboardDict.keys() :
                keyboardDict[char][0] = keyboardDict[char][0] + 1
                charCount = charCount + 1
            else :
                keyboardDict['unk'][0] = keyboardDict['unk'][0] + 1
                charCount = charCount + 1
        oFile2.write('[')
        for key in keyboardDict.keys() :
            keyboardDict[key][1] = keyboardDict[key][1] + keyboardDict[key][0]/charCount
            if key != 'unk' :
                oFile2.write('%s%s' % ((keyboardDict[key][0]/charCount), ', '))
            else :
                oFile2.write('%s' % ((keyboardDict[key][0]/charCount)))
            keyboardDict[key][0] = 0
        lineCount = lineCount + 1
        charCount = 0
        oFile2.write('], ')
    for key in keyboardDict.keys() :
        keyboardDict[key][1] = keyboardDict[key][1]/lineCount


oFile.write('%s%s' % ('commentDict = ', str(keyboardDict)))
oFile.close()
oFile2.close()

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
oFile = open('DictCode.py', 'w')
oFile2 = open('DictCodeLine.py', 'w')
for fileName in glob.glob("E:/school/ThesisProject/v.3/Code.md") :
    inFile = open(fileName, "r")
    for line in inFile :
        for i in range (0, line.__len__()) :
            char = line[i:i+1]
            char = char.lower()
            if char in keyboardDict.keys() :
                keyboardDict[char][0] = keyboardDict[char][0] + 1
                charCount = charCount + 1
            else :
                keyboardDict['unk'][0] = keyboardDict['unk'][0] + 1
                charCount = charCount + 1
        oFile2.write('[')
        for key in keyboardDict.keys() :
            keyboardDict[key][1] = keyboardDict[key][1] + keyboardDict[key][0]/charCount
            if key != 'unk' :
                oFile2.write('%s%s' % ((keyboardDict[key][0]/charCount), ', '))
            else :
                oFile2.write('%s' % ((keyboardDict[key][0]/charCount)))
            keyboardDict[key][0] = 0
        lineCount = lineCount + 1
        charCount = 0
        oFile2.write('], ')
    for key in keyboardDict.keys() :
        keyboardDict[key][1] = keyboardDict[key][1]/lineCount


oFile.write('%s%s' % ('codeDict = ', str(keyboardDict)))
oFile.close()
oFile2.close()