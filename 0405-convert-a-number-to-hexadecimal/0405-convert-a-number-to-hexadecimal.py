class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return '0'
        hexchar='0123456789abcdef'
        num&=0xffffffff
        op=''
        while num>0:
            op=hexchar[num&15]+op
            num>>=4
        return op