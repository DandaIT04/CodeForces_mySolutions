import math

class Solution(object):
    def theElephant(self,theValue):
        
        if theValue <= 5:
            print(1)
        else:
            if theValue % 5 == 0:
                print(math.floor(theValue/5))
            else:
                theResult = math.floor(theValue/5)
                print(theResult + 1)

theValue = int(input())

#theValue = 1000001

runSolution = Solution()

runSolution.theElephant(theValue)
