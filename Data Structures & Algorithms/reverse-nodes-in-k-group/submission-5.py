# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if we have at least k nodes
        def hasKNodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k
        
        # Reverse k nodes starting from head
        def reverseK(head, k):
            prev = None
            curr = head
            for _ in range(k):
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev, curr  # new_head, next_group_start
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while hasKNodes(prev_group.next, k):
            group_start = prev_group.next
            new_head, next_start = reverseK(group_start, k)
            
            # Connect previous group to new head
            prev_group.next = new_head
            # group_start is now the tail, connect to next group
            group_start.next = next_start
            # Move prev_group to the tail of current group
            prev_group = group_start
        
        return dummy.next
            
                
        