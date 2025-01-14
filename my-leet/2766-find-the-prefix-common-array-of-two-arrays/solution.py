class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        AM = 0
        BM = 0
        ans = []
        for i in range(len(A)):
            AM |= 1 << A[i]
            BM |= 1 << B[i]
            ans.append(bin(AM & BM).count('1'))
        return ans
