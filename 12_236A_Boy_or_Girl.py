class Solution(object):
    def distinct(self,theUsername): 
        
        discovered = []
        
        theUsername = list(dict.fromkeys(theUsername))
             
        if len(theUsername) % 2 == 0:
            print("CHAT WITH HER!")
        else:
            print("IGNORE HIM!")
               

theUsername = list(input())

#theUsername = list("sevenkplus")
#theUsername = list("wjmzbmr")
#theUsername = list("xiaodao")

runSolution = Solution()

runSolution.distinct(theUsername)

#https://www.w3schools.com/python/python_howto_remove_duplicates.asp

""" OLD Solution
class Solution(object):
    def distinct(self,theUsername,toPrint): 
        
        discovered = []
        
        for i in range(len(theUsername)):
            if theUsername[i] in discovered:
                theValue = theUsername[i]
                toPrint.remove(theValue)
            else:
                discovered.append(theUsername[i])
             
        if len(toPrint) % 2 == 0:
            print("CHAT WITH HER!")
        else:
            print("IGNORE HIM!")
               

theUsername = input()

#theUsername = list("sevenkplus")

toPrint = list(theUsername)

runSolution = Solution()

runSolution.distinct(theUsername,toPrint)
"""
