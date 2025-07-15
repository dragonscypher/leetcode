from functools import lru_cache

class Solution:
    def isValid(self, w: str) -> bool:
        if len(w) < 3:                       
            return False

        V = set('aeiouAEIOU')

        @lru_cache(None)                    
        def dfs(i: int, hv: bool, hc: bool) -> bool:
            if i == len(w):                  
                return hv and hc             

            c = w[i]
            if c.isdigit():                  
                return dfs(i + 1, hv, hc)
            if c.isalpha():                  
                return dfs(i + 1,
                           hv or c in V,
                           hc or c not in V)
            return False                     

        return dfs(0, False, False)

