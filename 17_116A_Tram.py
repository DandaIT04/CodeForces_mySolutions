class Solution(object):
    def minPassengers(self,theSum,theList):
    
        count = 0
        highestValue = 0
        accumulatedValue = 0
    
        while count < len(theList):
            accumulatedValue = accumulatedValue - int(theList[count][0])
            accumulatedValue = accumulatedValue + int(theList[count][1])
            if accumulatedValue>highestValue:
                highestValue = accumulatedValue
            count = count + 1
        print(highestValue)        
        
#theSum = int(input())

theSum = 10

theList = []

#while theSum != 0:
#    theSum -= 1
#    theList.append(input().split(' '))

theList.append(['0','5'])
theList.append(['1','7'])
theList.append(['10','8'])
theList.append(['5','3'])
theList.append(['0','5'])
theList.append(['3','3'])
theList.append(['8','8'])
theList.append(['0','6'])
theList.append(['10','1'])
theList.append(['9','0'])
    
runSolution = Solution()

runSolution.minPassengers(theSum,theList)
