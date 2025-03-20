from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)
        o = 0
        
        for i in c.values():
            if i % 2 != 0:
                o += 1
        
        return o <= 1

