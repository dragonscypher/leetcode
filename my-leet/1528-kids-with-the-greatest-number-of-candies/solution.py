class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        g=max(candies)
        for i in candies:
            if i+extraCandies >= g:
                a.append(True)
            else:
                a.append(False)
        return a        
