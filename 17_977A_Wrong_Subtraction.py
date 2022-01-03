import math

class Solution(object):
    def solveRemainder(self,theInput):
        count = 0
        
        while count != int(theInput[1]):
            count = count + 1
            
            if int(theInput[0]) % 10 == 0:
                theInput[0] = math.floor(int(theInput[0]) / 10)
            else:
                theInput[0] = int(theInput[0]) - 1
                
        print(theInput[0])        
        
theInput = input().split(' ')

runSolution = Solution()

runSolution.solveRemainder(theInput)
