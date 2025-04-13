class Solution:
    M = 10**9 + 7  
    def countGoodNumbers(self, n: int) -> int:
        def findPower(a, b):
            if b == 0:
                return 1
            half = findPower(a, b // 2) % self.M
            result = (half * half) % self.M
            if b % 2:
                result = (result * a) % self.M
            return result

        
        even_count = (n + 1) // 2  
        odd_count = n // 2        

        return (findPower(5, even_count) * findPower(4, odd_count)) % self.M
