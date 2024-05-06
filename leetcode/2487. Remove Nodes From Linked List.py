from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        m = head.val
        prev = head
        dummy = ListNode(0, prev)
        current = head.next

        while current:
            if current.val >= m:
                m = current.val
                prev.next = current
                prev = current
                current = current.next
            else:
                current = current.next
        prev.next = None

        return self.reverse(dummy.next)
    
    def reverse(self,head):
        prev = None
        current = head
        while current:
            _n = current.next
            current.next = prev
            prev = current
            current = _n
        
        return prev
        


        
        