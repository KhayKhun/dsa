# first try, beats 91.23%(time), 80.71%(memory)
def middleNode(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        length = 0

        while current:
            length += 1
            current = current.next
        mid = length // 2 + 1
        for i in range(0,mid - 1):
            head = head.next
            
        return head