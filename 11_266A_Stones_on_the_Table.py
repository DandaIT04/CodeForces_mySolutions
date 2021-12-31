class Solution(object):
    def stoneTable(self,theString):
        discovered = []
        
        changeValue = 0
        
        for count in range(len(theString)):
            undiscovered = theString[count]
            if len(discovered) != 0:
                if undiscovered == discovered[0]:
                    changeValue += 1
                    discovered = []
                    discovered.append(undiscovered)
                else:
                    discovered = []
                    discovered.append(undiscovered)
            else:
                discovered.append(undiscovered)
                
        print(changeValue)        

numOfString = int(input())

theString = input()

#theString = "BRBG"
    
runSolution = Solution()

runSolution.stoneTable(theString)
