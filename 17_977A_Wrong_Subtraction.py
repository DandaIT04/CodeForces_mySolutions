class Solution(object):
    def solveTen(self,theInput):
        count = 0
        
        while count != int(theInput[1]):
            
            while int(theInput[0]) % 10 == 0 and count != int(theInput[1]):
                theInput[0] = int(theInput[0]) / 10
                count = count + 1
            else:
                while int (theInput[0]) % 10 != 0 and count != int(theInput[1]):
                    count = count + 1
                    theInput[0] = int(theInput[0]) - 1
                
        print(int(theInput[0]))
        
theInput = input().split(' ')

runSolution = Solution()

runSolution.solveTen(theInput)
