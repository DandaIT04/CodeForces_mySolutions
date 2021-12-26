class Solution(object):
    def trueOrFalse(self,w):
        if w == 2:
            return "NO"
        else:    
            if(w % 2 != 0):
                return "NO"
            else:
                return "YES"

s = Solution()
w = input()
w = int(w)

print(s.trueOrFalse(w))     