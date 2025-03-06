class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        size = data.count(1)
        l = 0

        cur = 0
        swap = size

        for r in range(len(data)):

            cur += data[r]
            
            if r - l + 1 == size:
                swap = min(swap, size - cur)
                cur -= data[l]
                l += 1
        
        return swap
