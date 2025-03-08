class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        return min(s[i:i+k].count('W') for i in range(len(s)-k+1))
