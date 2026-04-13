class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        a=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                a=min(a,abs(i-start))
        return a