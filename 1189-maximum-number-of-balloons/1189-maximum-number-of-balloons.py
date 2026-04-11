class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        f={}
        for i in text:
            f[i]=f.get(i,0)+1
        return min(
            f.get('b',0),
            f.get('a',0),
            f.get('l',0)//2,
            f.get('o',0)//2,
            f.get('n',0),
        )
