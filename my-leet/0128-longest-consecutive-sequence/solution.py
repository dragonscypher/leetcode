class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a= set(sorted(nums))
        c=0
        for i in a:
            if i-1 not in a:
                l=1
                n=i
                while n+1 in a:
                    n+=1
                    l+=1
                c= max(l,c)
        return c
        
