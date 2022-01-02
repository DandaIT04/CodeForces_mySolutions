import math

class Solution(object):
    def majorityLower(self,theWord,theInput):
        theWord.sort()
        theValue = math.floor((len(theWord)/2)) + 1
        
        if len(theWord) % 2 == 0:
            if theWord[theValue-1].isupper():
                print(theInput.upper())
            else:
                print(theInput.lower())
        else:
            if len(theWord) == 1:
                print(theInput)
            else:    
                if theWord[theValue-1].isupper():
                    print(theInput.upper())
                else:
                    print(theInput.lower())            
        
theInput = input()

theWord = list(theInput)

#theInput = "KSXBXWpebh"

#theWord = list(theInput)

runSolution = Solution()

runSolution.majorityLower(theWord,theInput)
