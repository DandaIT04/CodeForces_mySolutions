# given string is s

class Solution(object):
    def solveSum(self,s):
        
        toPrint = ""
        
        for count,value in enumerate(s):
            if count == len(s) - 1:
                toPrint = toPrint + str(value)
            else:
                toPrint = toPrint + str(value) + "+"
        print(toPrint)        
        
s = sorted(list(map(int,input().split("+"))))

runSolution = Solution()

runSolution.solveSum(s)
