class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        a=0
        for i in arr: 
            if i%2 !=0: 
                a+=1
                if a==3:
                    return True
            else:
                a=0
        return False
        
