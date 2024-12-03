class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        a = []
        p = 0
        for i in spaces:
            a.append(s[p:i])
            p = i
        a.append(s[p:])
        return " ".join(a)

