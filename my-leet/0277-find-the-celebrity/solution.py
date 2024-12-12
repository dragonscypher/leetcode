
class Solution:
    def findCelebrity(self, n: int) -> int:
        l = 0
        r = n-1
        while l < r:
            if knows(l,r):
                l+=1 # l cannot be a celebrity, we discard it
            else:
                r-=1 # r cannot be a celebrity, we discard it

        # at this point l is a celebrity candidate, 
        # let's check if everyone knows him. 
        # If yes then l is a celebrity. Otherwise, there is no celebrity.
        for i in range(n):
            if i == l: continue
            if knows(l,i): return -1
            if not knows(i,l): return -1
        return l
