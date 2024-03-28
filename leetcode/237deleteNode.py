class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return str(self.val)
    
    def map(self):
        temp = []
        current = self
        while current:
            temp.append(str(current.val))
            current = current.next
        return " > ".join(temp)


a = ListNode(4)
b = ListNode(5)
c = ListNode(1)
d = ListNode(9)

a.next = b
b.next = c
c.next = d

class Solution:
    def deleteNode(self, node):
        current = node 
        while current.next:
            dummy = current
            _next = current.next
            _future = current.next.next

            current.val = current.next.val
            current = _next
            if _future: 
                dummy.next = _next
            else:
                dummy.next = None

print(a.map())
result = Solution().deleteNode(b)
print(a.map())