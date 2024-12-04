class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for idx, i in enumerate(nums):
            diff = target - i
            if diff in d:
                return [idx, d[diff]]
            d[i] = idx
        return []

