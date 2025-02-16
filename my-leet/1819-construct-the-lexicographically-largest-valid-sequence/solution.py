class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0]*(2*n-1)
        
        def fn(i): 
            
            if i == 2*n-1 or ans[i] and fn(i+1): return True 
            for x in reversed(range(1, n+1)): 
                if x not in ans: 
                    ii = x if x > 1 else 0 
                    if i+ii < 2*n-1 and ans[i] == ans[i+ii] == 0: 
                        ans[i] = ans[i+ii] = x
                        if fn(i+1): return True 
                        ans[i] = ans[i+ii] = 0 
        
        fn(0)
        return ans 
