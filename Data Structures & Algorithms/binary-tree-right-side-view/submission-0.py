# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])

        res = []
        while queue:
            level_size = len(queue)
            visible_el = 0

            for _ in range(level_size):
                node = queue.popleft()
                if _ == level_size-1:
                    visible_el = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(visible_el)

        return res