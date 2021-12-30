class Solution(object):
    def bitPlus(self,statement):
        theValue = 0
        for count,value in enumerate(statement):
            value.replace("x","")
            if "++" in value:
                theValue = theValue + 1
            else:
                theValue = theValue - 1
        return theValue    

noOfStatements = input()
noOfStatements = int(noOfStatements)

statement = []

while noOfStatements != 0:
    noOfStatements = noOfStatements - 1
    statement.append(input())

s = Solution()
print(s.bitPlus(statement))
