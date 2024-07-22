class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=OrderedDict()
        for i,j in zip(names, heights):
                a[j] = i
        a= OrderedDict( sorted (a.items(),reverse = True))
        return list(a.values())
        
