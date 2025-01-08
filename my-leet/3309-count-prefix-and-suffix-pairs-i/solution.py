class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            s1 = words[i]
            for j in range(i + 1, n):
                s2 = words[j]
                if len(s2) < len(s1):
                    continue
                p = s2[:len(s1)]
                s = s2[-len(s1):]
                if p == s1 and s == s1:
                    ans += 1
        return ans
