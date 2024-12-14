class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        window = Counter()
        res = left = 0
        for right, num in enumerate(nums):
            window[num] += 1
            while max(window) - min(window) > 2:
                if window[nums[left]] == 1:
                    window.pop(nums[left])
                else:
                    window[nums[left]] -= 1
                left += 1
            res += right - left + 1
        return res        
