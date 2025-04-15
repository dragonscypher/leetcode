class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        max_sub, pref_sums = 0, {0: -1}
        for i, sm in enumerate(accumulate(nums)):
            if sm - k in pref_sums:
                max_sub = max(max_sub, i - pref_sums[sm - k])
            if sm not in pref_sums:
                pref_sums[sm] = i
        return max_sub
