class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        a=[(j,i) for i, j in enumerate(nums)]
        heapify(a)
        for _ in range(k):
            _,i = heappop(a)
            nums[i] *= multiplier
            heappush(a,(nums[i],i))
        return nums
        
