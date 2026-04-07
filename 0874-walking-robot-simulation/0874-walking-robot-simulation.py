class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obs = set(map(tuple,obstacles))

        x=y=0
        d=0 #direstion
        md=0
        dirs=[(0,1),(1,0),(0,-1),(-1,0)] # N  E  S  W
        for i in commands:
            if i==-1:
                d = (d+1)%4
            elif i==-2:
                d = (d+3)%4
            else:
                dx,dy=dirs[d]
                for _ in range(i):
                    if(x+dx,y+dy) in obs:
                        break
                    x+=dx
                    y+=dy
                    md=max(md,x**2+y**2)
        return md