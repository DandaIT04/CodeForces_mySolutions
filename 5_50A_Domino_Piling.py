import math

class Solution(object):
    def domino(self,m):
        amount = int(m[0]) * int(m[1])
        result = math.floor(amount/2)
        print(result) 
        return result

m = input()
m = m.split()

s = Solution()

s.domino(m)