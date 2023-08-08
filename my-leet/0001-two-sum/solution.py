class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        back={}
        for i,j in enumerate(nums):
            d = target - j
            if d in back:
                return [back[d], i]
            back[j] = i


