class Solution(object):
    def nextRound(self,n,k):
        place = int(n[1])

        score = int(k[place-1])

        count = 0
        for i,value in enumerate(k):
            value = int(value)
            if value == 0:
                continue
            else: 
                if value >= score:
                    count = count + 1

        print(count)        

n = input()
n = n.split()

k = input()
k = k.split()

s = Solution()
s.nextRound(n,k)