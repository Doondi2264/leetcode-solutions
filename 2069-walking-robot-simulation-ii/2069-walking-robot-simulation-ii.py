class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.w=width
        self.h=height
        self.x=self.y=0
        self.d='East'

        

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        p=2*(self.w-1)+2*(self.h-1)
        num%=p
        if num==0:
            num=p
        while num>0:
            if self.d=="East":
                m=min(num,self.w-1-self.x)
                self.x+=m
                num-=m
                if num>0:
                    self.d='North'
            elif self.d=='North':
                m=min(num,self.h-1-self.y)
                self.y+=m
                num-=m
                if num>0:
                    self.d='West' #N
            elif self.d=='West':
                m=min(num,self.x)
                self.x-=m
                num-=m
                if num>0:
                    self.d="South"
            else:
                m=min(num,self.y)
                
                self.y-=m
                num-=m
                if num>0:
                    self.d='East'
        

    def getPos(self):
        """
        :rtype: List[int]
        """
        return [self.x,self.y]

    def getDir(self):
        """
        :rtype: str
        """
        return self.d


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()