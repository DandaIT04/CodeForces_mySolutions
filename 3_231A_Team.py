class Solution(object):
    def solveZeros(self,n):
        x = int(n)

        theResult = 0

        while x != 0:
            x = x-1
            n = input()
            n = str(n)
            if(n.count("1") > 1):
                theResult += 1

        return theResult
n = input()

n = int(n)

s = Solution()

print(s.solveZeros(n))