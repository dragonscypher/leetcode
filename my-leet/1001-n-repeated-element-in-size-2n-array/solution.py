class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] =1
        return max(a,key = a.get)

        
