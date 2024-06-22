class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ct=0
        for i in nums:
            if i != val:
                nums[ct] = i
                ct+=1
        return ct

