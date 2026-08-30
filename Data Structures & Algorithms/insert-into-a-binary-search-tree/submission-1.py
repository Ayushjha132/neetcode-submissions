# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # time: O(h)
        # space: O(1)

        if not root:
            return TreeNode(val)
        cur = root
        while True:
            if val < cur.val:
                if cur.left is not None:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    return root
            else:
                if cur.right is not None:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    return root
                