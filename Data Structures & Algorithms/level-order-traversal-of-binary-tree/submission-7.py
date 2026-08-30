# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        q = deque()
        q.append(root)

        while q:
            ls = []

            for i in range(len(q)):
                curr_node = q.popleft()
                ls.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                
            res.append(ls)
        
        return res