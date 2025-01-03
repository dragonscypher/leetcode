class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        m = 0
        for x, y in shift:
            if x == 0:
                m -= y
            else:
                m += y
        m %= len(s)
        return s[-m:] + s[:-m]
