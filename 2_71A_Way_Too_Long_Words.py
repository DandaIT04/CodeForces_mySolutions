class Solution(object):
    def solveWords(self,theArray):
        for count, value in enumerate(theArray):
            if len(value) > 10:
                theAnswer = len(value) - 2
                theAnswer = str(theAnswer)
                theArray[count] = value[0] + theAnswer + value[len(value) - 1]
                print(theArray[count])
            else:
                print(value)          

n = input()

toRepeat = int(n)

theArray = []

while toRepeat != 0:
    toRepeat = toRepeat - 1
    n = input()
    theArray.append(n)

s = Solution()

s.solveWords(theArray)

