class Solution:
    def romanToInt(self, s: str) -> int:
        rm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        num = rm[s[n - 1]]
        for i in range(n - 2, -1, -1):
            if rm[s[i]] >= rm[s[i + 1]]:
                num += rm[s[i]]
            else:
                num -= rm[s[i]]
        return num
