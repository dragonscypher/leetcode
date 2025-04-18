class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, count =len(nums), 0

        for i in range(n-2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                count += 1

        if nums[n-1] == 0 or nums[n-2] == 0:
            return -1

        return count
