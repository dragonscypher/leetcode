class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for idx in range(k-1):
           heapq.heappop(nums)
        return nums[0] * -1
        
