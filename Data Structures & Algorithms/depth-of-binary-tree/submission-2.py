# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = [0]
        def dfs(node, curr_count):
            if not node:
                max_depth[0] = max(curr_count - 1, max_depth[0])
                return

            dfs(node.left, curr_count + 1)
            dfs(node.right, curr_count + 1)
            

        dfs(root, 1)
        return max_depth[0]

