""" Original wrong code. Don't know why this doesn't work. No tutorials/solutions out there helps either
I initially thought it is related to ascii and it kinda does but does not at the same time?
if firstString = "aslkjlkasdd".lower()
and secondString = "asdlkjdajwi".lower()

even though ascii addition = 104 for both values so result should be 0, test case 5 for codeforces returns error because it should be 1 instead

class Solution(object):
    def stringSolve(self,firstString,secondString):
        firstStringValue = 0
        secondStringValue = 0
        
        for theFirstValues in firstString:
            theValue = ord(theFirstValues) - 96
            firstStringValue += theValue
        for theSecondValues in secondString:
            theValue = ord(theSecondValues) - 96
            secondStringValue += theValue
            
        if firstStringValue == secondStringValue:
            print("0")
        elif firstStringValue < secondStringValue:
            print("-1")
        else:
            print("1")
 
firstString = input().lower()
secondString = input().lower()
 
#firstString = "abCdeFg".lower()
#secondString = "abCdefghZZ".lower()
 
startSolution = Solution()
 
startSolution.stringSolve(firstString,secondString)
"""

class Solution(object):
    def stringSolve(self,firstString,secondString):
            
        if firstString == secondString:
            print("0")
        elif firstString < secondString:
            print("-1")
        else:
            print("1")
 
firstString = input().lower()
secondString = input().lower()
 
#firstString = "aslkjlkasdd".lower()
#secondString = "asdlkjdajwi".lower()
 
startSolution = Solution()
 
startSolution.stringSolve(firstString,secondString)
