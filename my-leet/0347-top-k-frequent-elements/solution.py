class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a= Counter(nums)
        a= sorted(a.items(), key=lambda x: -x[1])
        o= [i for i, count in a[:k]]
        return o
