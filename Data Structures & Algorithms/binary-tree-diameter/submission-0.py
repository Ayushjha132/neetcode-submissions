# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        self.maxL = 0 # global access 
        

        def height(root):
            if not root: return 0
            left_height = height(root.left)
            right_height = height(root.right)

            self.maxL = max(self.maxL, left_height + right_height)
            return 1 + max(left_height, right_height)

        height(root)

        return self.maxL
        
        