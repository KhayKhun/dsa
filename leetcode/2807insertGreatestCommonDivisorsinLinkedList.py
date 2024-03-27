# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return str(self.val)

x = ListNode(18,ListNode(6,ListNode(10,ListNode(3))))

class Solution:
    def insertGreatestCommonDivisors(self, head):
        current = head
        while current.next:
            _next = current.next
            gcd_node = ListNode(self.getGCD(current.val,_next.val))
            
            current.next = gcd_node
            gcd_node.next = _next
            current = _next
        
        return head


    def getGCD(self, a, b):
        while b:
            a, b = b, a % b
        return a

result = Solution().insertGreatestCommonDivisors(ListNode(x))  
print(result,result.next)