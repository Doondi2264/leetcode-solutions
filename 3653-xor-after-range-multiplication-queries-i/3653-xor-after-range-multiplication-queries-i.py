class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        m=(10**9)+7
        for l,r,k,v in queries:
            
            for i in range(l,r+1,k):
                nums[i]=(nums[i]*v)%m
                
        a=0
        for i in nums:
            a^=i
        return a