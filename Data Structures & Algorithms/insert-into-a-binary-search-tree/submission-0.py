# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        cur = root
        while True:
            if val < cur.val and cur.left is not None:
                cur = cur.left
            elif val > cur.val and cur.right is not None:
                cur = cur.right
            else:
                if val < cur.val:
                    cur.left = TreeNode(val)
                    return root
                else:
                    cur.right = TreeNode(val)
                    return root
