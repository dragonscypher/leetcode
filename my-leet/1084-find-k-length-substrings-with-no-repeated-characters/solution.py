class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            if r - l + 1 == k:
                res += int(sum(count.values()) == len(count))
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
        return res
