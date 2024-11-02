class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s= sentence.split(" ")
        n=len(s)
        l=s[n-1][-1]
        for i in range(n):
            if s[i][0] !=l:
                return False
            l=s[i][-1]
        return True
