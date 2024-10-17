class Solution:
    def maximumSwap(self, num: int) -> int:
        a = list(str(num))
        n = len(a)
        left, right = -1, -1
        max_idx = n - 1
        for i in range(n - 2, -1, -1):
            if a[i] > a[max_idx]:
                max_idx = i
            elif a[i] < a[max_idx]:
                left, right = i, max_idx
        
        if left != -1:
            a[left], a[right] = a[right], a[left]
        
        return int(''.join(a))

