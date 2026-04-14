class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort()
        memo={}
        def dp(i,j):
            if(i,j)in memo:
                return memo[(i,j)]
            if i==len(robot):
                return 0
            if j==len(factory):
                return float('inf')
            r=dp(i,j+1)
            p,l=factory[j]
            c=0
            for k in range(l):
                if i+k>=len(robot):
                    break
                c+=abs(robot[i+k]-p)
                r=min(r,c+dp(i+k+1,j+1))
            memo[(i,j)]=r
            return r
        return dp(0,0)