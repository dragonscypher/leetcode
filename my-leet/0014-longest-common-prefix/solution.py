class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        o=""
        p=sorted(strs)
        f=p[0]
        l=p[-1]
        for i in range (min(len(f),len(l))):
            
            if (f[i] != l[i]):
                return o
            o+=f[i]
        return o
            



