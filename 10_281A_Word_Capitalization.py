class Solution(object):
    def capFirstWord(self,word):
        
        if word[0].isupper() is True:
            print(word)
        else:
            theWord = word[0].capitalize()
            word = word[1:]
            newWord = theWord + word
            print(newWord)
        
word = input()

#word = "aBCD"

runSolution = Solution()

runSolution.capFirstWord(word)
