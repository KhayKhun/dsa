# Definition for singly-linked list.
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


x = ListNode(1,ListNode(1,ListNode(2)))
class Solution:
    def deleteDuplicates(self, head):
        value = None
        prev = ListNode(0)
        current = head

        while current:
            if current.val == value:
                prev.next = current.next
                current = current.next
            else:
                dummy = current
                value = current.val
                current = current.next
                prev = dummy
        
        return head


print(x.map())
result = Solution().deleteDuplicates(x)
print(result.map())