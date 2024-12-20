class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while nums[r] * (r - l + 1) > cur_sum + k:
                cur_sum -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res
