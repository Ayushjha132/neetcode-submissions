# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        if not root: return []

        def dfs(node):
            cur = node.val
            nonlocal res
            res.append(cur)

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        dfs(root)

        res.sort()

        return res[k-1]
