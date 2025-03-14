class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        candies.sort(reverse = True)
        n = len(candies)
        l, r = 0, candies[0]
        while l < r:
            m = (l + r + 1) // 2
            print(l, r, m)
            cnt, ptr = 0, 0
            while ptr < n and candies[ptr] >= m:
                cnt += candies[ptr] // m
                ptr += 1
            if cnt >= k:
                l = m
            else:
                r = m - 1
        return l
