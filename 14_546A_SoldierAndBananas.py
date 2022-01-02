class Solution(object):
    def banana(self,theList):
        theCost = 0
        
        for count in range(int(theList[2])):
            theValue = count + 1
            theCost = theCost + (theValue * int(theList[0]))
                          
        hisWallet = int(theList[1])
        
        if hisWallet >= theCost:
            print(0)
        else:  
            toPrint = abs(hisWallet - theCost)
            print(toPrint)

#theList = input().split()

theList = "3 17 4".split()

runSolution = Solution()

runSolution.banana(theList)
