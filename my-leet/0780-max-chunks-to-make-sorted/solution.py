class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        pm = arr[:]
        sm = arr[:]

        
        for i in range(1, n):
            pm[i] = max(pm[i - 1], pm[i])

        
        for i in range(n - 2, -1, -1):
            sm[i] = min(sm[i + 1], sm[i])

        c = 0
        for i in range(n):
            
            if i == 0 or sm[i] > pm[i - 1]:
                c += 1

        return c
