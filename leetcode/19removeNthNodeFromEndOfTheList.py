class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# my solution(beat 13%) :)
def removeNthFromEnd(head, n):
    """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
    """
    # list nodes to array
    temp = []
    current_node = head
    while current_node:
        temp.append(current_node.val)
        current_node = current_node.next
        
    # remove the nth val from array
    temp.pop(-(n))
    
    # array to list nodes
    dummy = ListNode(0)
    current = dummy
    for i in temp:
        current.next = ListNode(i)
        current = current.next    
    
    return dummy.next
    
# other solutin
def removeNthFromEnd(head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
    
# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
n = 2

removeNthFromEnd(head, n)