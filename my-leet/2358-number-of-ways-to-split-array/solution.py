class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        current_sum = count = 0

        for ind, num in enumerate(nums[:-1]):
            current_sum += num
            if current_sum >= nums_sum - current_sum:
                count += 1
        
        return count
