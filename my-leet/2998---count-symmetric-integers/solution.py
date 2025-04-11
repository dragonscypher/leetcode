class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum(
            
            sum(map(int, str(x)[:n // 2])) 
            ==
            sum(map(int, str(x)[n // 2:]))
            
            for x in range(low, high + 1) 
                if (n := len(str(x))) % 2 == 0
        )
        
