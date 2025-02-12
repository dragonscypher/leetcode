class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        m = {}
        res = -1

        for num in nums:
            tmp, tmpNum = 0, num
            while tmpNum > 0:
                tmp += tmpNum % 10
                tmpNum //= 10
            
            if tmp in m:
                res = max(res, num + m[tmp])
                if num > m[tmp]:
                    m[tmp] = num
            else:
                m[tmp] = num
        
        return res
