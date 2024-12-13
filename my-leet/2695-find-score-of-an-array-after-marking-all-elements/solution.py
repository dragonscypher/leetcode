class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
       
        h = [(nums[i], i) for i in range(n)]
        heapq.heapify(h)
        
        m = [False] * n  
        s = 0

        while h:
            v, i = heapq.heappop(h) 
            if m[i]:
                continue

            s += v
            m[i] = True
            if i - 1 >= 0:
                m[i - 1] = True
            if i + 1 < n:
                m[i + 1] = True

        return s


