class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n,m = len(str1), len(str2)
        a=['?']*(n+m-1)

        for i,b in enumerate(str1):
            if b!='T':
                continue
            for j,c in enumerate(str2):
                v=a[i+j]
                if v!='?' and v!=c:
                    return ""
                a[i+j]=c
        o=a
        a=['a' if c=='?' else c for c in a]

        for i,b in enumerate(str1):
            if b!='F':
                continue
            if ''.join(a[i:i+m]) !=str2:
                continue
            for j in range(i+m-1,i-1,-1):
                if o[j]   =='?':
                    a[j]='b'
                    break
            else:
                return ""
        return ''.join(a)