"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        clone = {}
        curr = head
        while curr:
            clone[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new_node = clone[curr]
            if curr.next:
                new_node.next = clone[curr.next]
            if curr.random:
                new_node.random = clone[curr.random]
            curr = curr.next
        
        return clone[head]
