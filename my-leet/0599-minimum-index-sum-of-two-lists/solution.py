class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a = {}
        
        # Using enumerate to get both the value and its index
        for index1, value1 in enumerate(list1):
            if value1 in list2:
                index2 = list2.index(value1)
                a[value1] = index1 + index2

        # Filter keys that have the minimum value in a
        min_val = min(a.values())
        return [key for key, val in a.items() if val == min_val]
