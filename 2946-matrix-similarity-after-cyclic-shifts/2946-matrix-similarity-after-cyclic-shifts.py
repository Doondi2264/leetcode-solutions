class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        m,n=len(mat),len(mat[0])
        k = k%n
        if k==0:
            return True
        for i in range(m):
            r=mat[i]
            if i%2==0:
                s=r[k:]+r[:k]
            else:
                s=r[-k:]+r[:-k]
            if s!=r:
                return False
        return True
