class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        current = self
        temp = []
        while current:
            temp.append("[%s]" %current.val)
            current = current.next
        return '->'.join(temp)
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

# my solution (Beats 92.64% of users with Python3)  
def swapPairs(head : ListNode) -> ListNode:
    current = head
    firstTime = True
    prev = ListNode(0)
    
    while current and current.next: # 1 2 3 4
        if firstTime:
            head = current.next # 2
            firstTime = False
            
        over_node = current.next.next # store 
        
        current.next.next = current  
        # (2) reconnect the previous nodes with new switched order 
        prev.next = current.next      
        current.next = over_node
        # (1) store the previous switched node as prev, to reconnect when the switch completed in future nodes
        prev = current 
        current = current.next
        
    return head

print(swapPairs(head))