class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=0
        if len(s)==len(t) and sorted(s) == sorted(t):
            return True
        else:
            return False

