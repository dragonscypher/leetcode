class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        e = set()
        a = 0
        for i in range(26):
            l = s.find(chr(ord('a') + i))
            if l != -1:
                r = s.rfind(chr(ord('a') + i))
                if r - l < 2:
                    continue
                for j in range(l + 1, r):
                    e.add(s[j])
                    if len(e) == 26:
                        break
                a += len(e)
                e.clear()
        return a
