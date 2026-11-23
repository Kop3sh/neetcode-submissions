# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def rev(h):
            prev, curr = None, h
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        def trav(h):
            while h:
                print(h.val)
                h = h.next
        

        i = 1
        dummy = rev(head)
        trav(dummy)
        prev, curr = None, dummy
        while i < n and curr:
            prev, curr = curr, curr.next
            i += 1

        if i == 1 and n == 1:
            return rev(dummy.next if dummy.next else None)

        if curr == None:
            prev.next = None
        else:
            prev.next = curr.next
        curr.next = None

        return rev(dummy)
        