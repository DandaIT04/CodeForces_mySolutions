class Solution(object):
    def weightMore(self,theList):
        
        theAnswer = 0
        
        while int(theList[0]) <= int(theList[1]):
            theAnswer += 1
            theList[0] = int(theList[0]) * 3
            theList[1] = int(theList[1]) * 2
        
        print(theAnswer)    
        
theList = input().split(" ")

#theList = "4 7".split(" ")
#theList = "4 9".split(" ")
#theList = "1 1".split(" ")

runSolution = Solution()

runSolution.weightMore(theList)
