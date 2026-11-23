# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self, node, n):
        if not node:
            return None, 0
        
        node.next, pos_end = self.rec(node.next, n)
        pos_end += 1
        if pos_end == n:
            return node.next, pos_end
        return node, pos_end

        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res, _ = self.rec(head, n)
        return res
        
