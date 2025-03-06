class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
         n, ans = len(grid), {}  
         [ans.update({num: ans.get(num, 0) + 1}) for g in grid for num in g] 
         return [next(k for k, v in ans.items() if v == 2), next(i for i in range(1, n**2 + 1) if i not in ans)] 
