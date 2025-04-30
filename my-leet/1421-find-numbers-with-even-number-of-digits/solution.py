class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            stringConv = len(str(nums[i]))
            if not stringConv%2:
                count += 1
        return count 
