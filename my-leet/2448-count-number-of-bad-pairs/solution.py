

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        t = len(nums) * (len(nums) - 1) // 2  
        freq = defaultdict(int)
        g = 0

        for i, num in enumerate(nums):
            key = num - i 
            g += freq[key] 
            freq[key] += 1  
        return t - g  
