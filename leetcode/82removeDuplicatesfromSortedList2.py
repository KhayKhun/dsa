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


x = ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5,ListNode(5))))))))

class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        dummy = ListNode()
        prev = dummy
        current = head
        while current and current.next:
            # duplicated case
            if current.val == current.next.val:
                # move current until there is no duplicate
                while current.next and current.val == current.next.val:
                    current = current.next
                
                # if there is no more duplicate, follow the prev along
                prev.next = current.next
                current = current.next

            # not duplicated case
            else:
                # step forward the prev and current normally
                prev.next = current
                prev = current
                current = current.next


        return dummy.next


print(x.map())
result = Solution().deleteDuplicates(x)
print(result.map())