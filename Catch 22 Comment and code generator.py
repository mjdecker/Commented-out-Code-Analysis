import sys
import glob

count = 0
outFile = open("Code.md", "w")

for fileName in glob.glob("E:/school/ThesisProject/blah/*.c") :
    inFile = open(fileName, "r")
    for line in inFile :
        for i in range (0, line.__len__() - 1) :
                val = "%s%s" % (i, i + 1)
                if val == "//" :
                        count = 1
                if val == "/*" :
                        count = 2
                if val == "*/" :
                        count = 1
        
        if count == 0 :
                outFile.write(line + "\n")
        if count == 1 :
                count = 0
