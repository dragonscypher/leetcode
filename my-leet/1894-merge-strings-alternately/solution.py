class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=[]
        n= max(len(word1), len(word2))
        for i in range(n):      
            if i<len(word1): a+=  word1[i]
            if i<len(word2): a+=word2[i]
        return "".join(a)
