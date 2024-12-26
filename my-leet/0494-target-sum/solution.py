class Solution:
    def findTargetSumWays(self, a: List[int], t: int) -> int:
        return (f:=cache(lambda i,z:f(i+1,z+a[i])+f(i+1,z-a[i]) if a[i:] else z==t))(0,0)
