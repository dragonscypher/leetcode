class Solution(object):
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def traverse(root):
            if not root:
                return

            total_children = len(root.children)
            for i in range (total_children):
                traverse(root.children[i])
            res.append(root.val)
        traverse(root)
        return res
            
