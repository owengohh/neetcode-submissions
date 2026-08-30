# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r_no1 = ""
        r_no2 = ""

        curr = l1
        while curr:
            r_no1 += str(curr.val)
            curr = curr.next
        
        curr = l2
        while curr:
            r_no2 += str(curr.val)
            curr = curr.next
        
        no1 = int(r_no1[::-1])
        no2 = int(r_no2[::-1])

        int_res = no1 + no2

        res = ListNode()
        curr = res

        for ch in str(int_res)[::-1]:
            node = ListNode(int(ch))
            curr.next = node
            curr = curr.next
        
        return res.next


