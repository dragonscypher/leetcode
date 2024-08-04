import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 1000000007
        pq = [(num, i, i) for i, num in enumerate(nums)]
        heapq.heapify(pq)
        
        result = 0
        for i in range(1, right + 1):
            current_sum, start, end = heapq.heappop(pq)
            if i >= left:
                result = (result + current_sum) % MOD
            
            if end < n - 1:
                heapq.heappush(pq, (current_sum + nums[end + 1], start, end + 1))
        
        return result

