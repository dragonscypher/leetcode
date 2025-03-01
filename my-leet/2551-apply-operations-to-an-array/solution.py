class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                [nums[index], nums[i]] = [nums[i], nums[index]]
                index += 1
        
        return nums
