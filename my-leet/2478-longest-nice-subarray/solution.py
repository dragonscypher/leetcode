class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len = 1
        for right, used_bits in enumerate(nums): 
            left = right - 1
            while left >= 0 and used_bits & nums[left] == 0: 
                used_bits |= nums[left] 
                left -= 1 
            max_len = max(max_len, right - left)
            
        return max_len
