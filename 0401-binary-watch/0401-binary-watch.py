class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        op=[]
        for h in range(12):
            for m in range(60):
                if (bin(h).count('1') + bin(m).count('1'))==turnedOn:
                    op.append("{}:{:02d}".format(h,m))
        return op