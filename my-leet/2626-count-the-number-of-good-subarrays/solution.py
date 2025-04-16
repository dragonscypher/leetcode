from collections import Counter

class Solution:
    def countGood(self, A: List[int], k: int) -> int:
        N, count = len(A), Counter()
        L =  result = pair_count = 0

        for i, v in enumerate(A):
            pair_count += count[v]
            count[v] += 1
            while L < i and pair_count >= k:
                result += N - i
                count[A[L]] -= 1
                pair_count -= count[A[L]]
                L += 1
        return result
