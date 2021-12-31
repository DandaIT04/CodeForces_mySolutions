""" My Fastest Solution 92MS """
class Solution(object):
    def solveMatrix(self,theMatrix):
        positionValue = []
        
        if "1" in theMatrix[2][2]:
            print(0)
        else:
            if "1" in theMatrix[0]:
                positionValue.append(0)
                positionValue.append(theMatrix[0].index("1"))
                
            elif "1" in theMatrix[1]:
                positionValue.append(1)
                positionValue.append(theMatrix[1].index("1"))
                        
            elif "1" in theMatrix[2]:
                positionValue.append(2)
                positionValue.append(theMatrix[2].index("1"))
                        
            elif "1" in theMatrix[3]:
                positionValue.append(3)
                positionValue.append(theMatrix[3].index("1"))
                        
            elif "1" in theMatrix[4]:
                positionValue.append(4)  
                positionValue.append(theMatrix[4].index("1"))
                        
            finalValue = 0
            
            firstPosValue = positionValue[0]
            secondPosValue = positionValue[1]
            
            while firstPosValue < 2:
                finalValue = finalValue + 2 - firstPosValue
                firstPosValue = 2
            while firstPosValue > 2:
                finalValue = finalValue + firstPosValue - 2
                firstPosValue = 2
            while secondPosValue < 2:
                finalValue = finalValue + 2 - secondPosValue
                secondPosValue = 2
            while secondPosValue > 2:
                finalValue = finalValue + secondPosValue - 2
                secondPosValue = 2
                
            print(finalValue)
            
#theMatrix = [["1","0","0","0","0"],
#["0","0","0","0","0"],
#["0","0","0","0","0"],
#["0","0","0","0","0"],
#["0","0","0","0","0"]]
        
theMatrix = []

totalRows = 5

while totalRows != 0:
    totalRows -= 1
    theMatrix.append(list(map(str,input().split())))

theSolution = Solution()

theSolution.solveMatrix(theMatrix)

""" First Improvement from 218MS to 186MS """
"""
class Solution(object):
    def solveMatrix(self,theMatrix):
        positionValue = []
        
        if "1" in theMatrix[0]:
            positionValue.append(0)            
            for count,value in enumerate(theMatrix[0]):
                if value == "1":
                    positionValue.append(count)
            
        elif "1" in theMatrix[1]:
            positionValue.append(1)
            for count,value in enumerate(theMatrix[1]):
                if value == "1":
                    positionValue.append(count)
                    
        elif "1" in theMatrix[2]:
            positionValue.append(2)
            for count,value in enumerate(theMatrix[2]):
                if value == "1":
                    positionValue.append(count)
                    
        elif "1" in theMatrix[3]:
            positionValue.append(3)
            for count,value in enumerate(theMatrix[3]):
                if value == "1":
                    positionValue.append(count)
                    
        elif "1" in theMatrix[4]:
            positionValue.append(4)  
            for count,value in enumerate(theMatrix[4]):
                if value == "1":
                    positionValue.append(count)
                    
        finalValue = 0
        
        firstPosValue = positionValue[0]
        secondPosValue = positionValue[1]
        
        while firstPosValue < 2:
            firstPosValue += 1
            finalValue += 1
        while firstPosValue > 2:
            firstPosValue -= 1
            finalValue += 1
        while secondPosValue < 2:
            secondPosValue += 1
            finalValue += 1
        while secondPosValue > 2:
            secondPosValue -= 1
            finalValue += 1
            
        print(finalValue)

#theMatrix = [["0","0","0","0","0"],
#["0","0","1","0","0"],
#["0","0","0","0","0"],
#["0","0","0","0","0"],
#["0","0","0","0","0"]]
        
theMatrix = []

totalRows = 5

while totalRows != 0:
    totalRows -= 1
    theMatrix.append(list(map(str,input().split())))

theSolution = Solution()

theSolution.solveMatrix(theMatrix)
"""

""" My first solution, very inefficient 218MS """
"""
class Solution(object):
    def solveMatrix(self,theMatrix):
        positionValue = []
        
        for count1, value1 in enumerate(theMatrix):
            if len(positionValue) == 2:
                break
            else:
                for count2, value2 in enumerate(value1):
                    for count3,value3 in enumerate(value2):
                        if len(positionValue) == 2:
                            break
                        else:
                            if value3 == "1":
                                positionValue.append(count2)
                                positionValue.append(count1)

        finalValue = 0
        
        firstPosValue = positionValue[0]
        secondPosValue = positionValue[1]
        
        while firstPosValue < 2:
            firstPosValue += 1
            finalValue += 1
        while firstPosValue > 2:
            firstPosValue -= 1
            finalValue += 1
        while secondPosValue < 2:
            secondPosValue += 1
            finalValue += 1
        while secondPosValue > 2:
            secondPosValue -= 1
            finalValue += 1
            
        print(finalValue)
        
theMatrix = []

totalRows = 5

while totalRows != 0:
    totalRows -= 1
    theMatrix.append(list(map(str,input().split())))
    
theSolution = Solution()

theSolution.solveMatrix(theMatrix)
"""
