# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# my solution 
class Solution:
    def mergeTwoLists(self, list1,list2):
        dummy = ListNode()
        current = dummy
        while list1 and list2:               
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
            else:
                current.next = list2
                list2, current = list2.next, list2
                
        if list1 or list2:
            current.next = list1 if list1 else list2
            
        return dummy.next
def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(5)
list1.next.next.next.next = ListNode(6)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = None
list4 = None

list5 = None
list6 = ListNode(0)

solution = Solution()
print(print_linked_list(solution.mergeTwoLists(list1, list2)))
print(print_linked_list(solution.mergeTwoLists(list3, list4)))
print(print_linked_list(solution.mergeTwoLists(list5, list6)))
