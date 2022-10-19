class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for a,b in enumerate(nums):
            m=target-b
            if m in hmap:
                return [hmap[m],a]
            hmap[b] = a
        return
