class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        sc=[0]*(n+1)
        for i,j in trust:
            sc[i]-=1
            sc[j]+=1
        for i in range(1,n+1):
            if sc[i]==n-1:
                return i
        return -1