class Solution:
    def tupleSameProduct(self, a: List[int]) -> int:
        return 8*sum(comb(v,2) for v in Counter(map(prod,combinations(a,2))).values())
