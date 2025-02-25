class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod, n = 10 ** 9 + 7, len(arr)
        x, y, cummulative_sum, res = 0, 1, 0, 0
        for num in arr:
            cummulative_sum += num 
            if cummulative_sum % 2 == 1: 
                x += 1
                res += y % mod
            else: 
                y += 1
                res += x % mod
        res %= mod
        return res
