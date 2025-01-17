class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        c = derived[0]
        for i in range(1,len(derived)):
            c = c ^ derived[i]
        return c == 0
