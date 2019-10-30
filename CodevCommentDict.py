import DictComments
import DictCode
import sys

oFile = open("resultsCvCDict.md", "w")

for key in DictCode.codeDict.keys() :
    if DictCode.codeDict[key][1] > DictComments.commentDict[key][1] :
        oFile.write("%s %s%s%s %s %s %s" % ("Key is", "[", key, "]", "Code is larger by:", DictCode.codeDict[key][1] - DictComments.commentDict[key][1], "\n"))
    else :
        oFile.write("%s %s%s%s %s %s %s" % ("Key is", "[", key, "]", "Comment is larger by:", DictComments.commentDict[key][1] - DictCode.codeDict[key][1], "\n"))

oFile.close()

