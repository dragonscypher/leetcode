class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ca=cb=cc=0
        l=a+b+c
        r=[]
        if l>0:
            for i in range(l):
                if (a>=b and a>=c and ca !=2) or (a>0 and (cb==2 or cc==2)):
                    r.append('a')
                    a-=1
                    ca+=1
                    cb=0
                    cc=0
                elif (b>=c and b>=a and cb !=2) or (b>0 and (ca==2 or cc==2)):
                    r.append('b')
                    b-=1
                    cb+=1
                    ca=0
                    cc=0
                elif (c>=b and c>=a and cc !=2) or (c>0 and (cb==2 or ca==2)):
                    r.append('c')
                    c-=1
                    cc+=1
                    cb=0
                    ca=0
        return "".join(r)

        
