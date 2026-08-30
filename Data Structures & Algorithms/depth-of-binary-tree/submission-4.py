# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        longest = [0]
        def dfs(node, count):
            if not node:
                longest[0] = max(count, longest[0])
                return
            
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)
        dfs(root, 0)
        return longest[0]
            