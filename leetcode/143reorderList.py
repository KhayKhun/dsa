class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return "<%s>" % self.val
    def map(self):
        current = self
        res = []
        while current:
            res.append(current.val)
            current = current.next
        return res    
    
class Solution:    
    def reorderList(self, head,size = 0):
        if size == 0: size = self.getSize(head)
        if size <3 : return
        current = head
        
        before_last = None
        last = None
        
        for i in range(size-2):
            before_last = current.next
            current = current.next
        last = current.next
        before_last.next = None
        
        last.next = head.next
        head.next = last
        
        if last.next.next:
            self.reorderList(last.next,size -2)

    
    def getSize(self,head):
        self.count += 1
        size = 0
        while head:
            size += 1
            head = head.next
        return size
        
x = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7,ListNode(8,ListNode(9)))))))))
# x = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
# x = ListNode(1,ListNode(2))

s = Solution()
print(x.map())
s.reorderList(x)
print(x.map())

# other's solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Function for reversing
    def reverse(self, head):
        prev = None
        current = head
        while current:
            prev, prev.next, current = current, prev, current.next
        return prev
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        fast = head.next
        slow = head
        # Catch the Middle of List (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Cut Middle of list then Reverse it
        rev = self.reverse(slow.next)
        slow.next = None

        while rev:
            h_next = head.next
            r_next = rev.next
            head.next = rev
            rev.next = h_next
            rev = r_next
            head = h_next  