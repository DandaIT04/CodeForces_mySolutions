import math

class Solution(object):
    def majorityLower(self,theWord,theInput):
        newList = list(theWord)
        newList.sort()
        theValue = math.floor((len(newList)/2)) + 1
        
        if len(newList) % 2 == 0:
            if newList[theValue-1].isupper():
                print(theInput.upper())
            else:
                print(theInput.lower())
        else:
            if len(newList) == 1:
                print(theInput)
            else:    
                if newList[theValue-1].isupper():
                    print(theInput.upper())
                else:
                    print(theInput.lower())            
        
#theInput = input()

#theWord = list(theInput)

theInput = "KSXBXWpebh"

theWord = list(theInput)

runSolution = Solution()

runSolution.majorityLower(theWord,theInput)
