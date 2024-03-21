
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self) -> str:
        return '[%s]' %self.val
        
x = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))

def reverseList(head):
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    
    dummy = ListNode()
    current = dummy
    while len(stack) > 0:
        newNode = ListNode(stack.pop())
        current.next = newNode
        current = current.next
        
    return dummy.next


print(x,x.next,x.next.next,x.next.next.next)
res = reverseList(x)
print(res,res.next,res.next.next,res.next.next.next)