# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = [0]

        def dfs(node, count):
            if not node:
                max_depth[0] = max(max_depth[0], count)
                return
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)
        
        dfs(root, 0)
        return max_depth[0]

            