from functools import lru_cache
class Solution:
    def minimumDistance(self, word: str) -> int:
        
        def getPos(c):
            i=ord(c)-ord('A')
            return (i//6,i%6)
        
        def dist(a,b):
            if a is None:
                return 0
            x1,y1=getPos(a)
            x2,y2=getPos(b)
            return abs(x1-x2)+abs(y1-y2)
        @lru_cache(None)
        def dp(i,f1,f2):
            if i==len(word):
                return 0
            c=word[i]
            # finger 1 movement
            cost1=dist(f1,c)+dp(i+1,c,f2)

            # finger 2 movement
            cost2=dist(f2,c)+dp(i+1,f1,c)
            return min(cost1,cost2)
        return dp(0,None,None)
