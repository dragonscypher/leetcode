# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:    return []
        ans = []
        st = [root]
        while st:
            l = []
            for i in st:
                if i.left:
                    l.append(i.left)
                if i.right:
                    l.append(i.right)
            ans.append([i.val for i in st])
            st = l[:]
        
        def min_swaps(arr):
            ans = 0
            new_arr = [(arr[i], i) for i in range(len(arr))]
            new_arr.sort(key = lambda x: x[0])
            vis = set()
            for i in range(len(arr)):
                if new_arr[i][1] == i or i in vis:
                    continue
                cycle, j = 0, i
                while j not in vis:
                    vis.add(j)
                    j = new_arr[j][1]
                    cycle += 1
                
                if cycle > 0:
                    ans += (cycle - 1)

            return ans

        c = 0
        for i in ans:
            if i == sorted(i):
                continue
            c += min_swaps(i)
            

        return c
