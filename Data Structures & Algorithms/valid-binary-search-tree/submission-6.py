# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(l, r, node):
            if not node: return True
            if node.val <= l or node.val >= r:
                return False
            return dfs(l, node.val, node.left) and dfs(node.val, r, node.right)
        
        return dfs(float('-inf'), float('inf'), root)