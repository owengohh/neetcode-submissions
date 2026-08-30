# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [None]
        count = [0]
        def dfs(node):
            if not node or res[0] is not None:
                return
            
            dfs(node.left)

            count[0] += 1
            if count[0] == k:
                res[0] = node.val
                return
            
            dfs(node.right)
        
        dfs(root)
        return res[0]