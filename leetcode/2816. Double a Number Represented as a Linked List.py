# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        
        current = head
        carry = 0
        while current:
            total = carry + 2 * current.val
            current.val = total % 10
            carry = total//10 if total > 9 else 0
            if not current.next and carry > 0:
                current.next = ListNode(carry)
                break
            current = current.next
        
        return self.reverse(head)
    
    def reverse(self, head):
        prev = None
        while head:
            _n = head.next
            head.next = prev
            prev = head
            head = _n
        return prev
        