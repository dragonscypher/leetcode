class Solution:

    def majorityElement(self, nums: List[int]) -> int:

        count = 0

        for i in range(0, len(nums)):
            if(count == 0):
                count = 1
                majority = nums[i]
            else:
                if(nums[i] == majority):
                    count += 1
                else:
                    count -= 1
        
        return majority
        
