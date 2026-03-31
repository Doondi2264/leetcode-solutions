class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        _5=0
        _10=0
        for i in bills:
            if i == 5:
                _5+=1
            elif i==10:
                if _5==0:
                    return False
                _5-=1
                _10+=1
            else:
                if _10>0 and _5>0:
                    _5-=1
                    _10-=1
                elif _5>=3:
                    _5-=3
                else:
                    return False
        return True