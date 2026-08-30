# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        
        def dfs(node):
            if not node:
                return
            if node.val >= p.val and node.val <= q.val:
                return node
            
            if node.left and p.val < node.val and q.val < node.val:
                return dfs(node.left)
            
            if node.right and p.val > node.val and q.val > node.val:
                return dfs(node.right)
        
        return dfs(root)
        