from time import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ChatGPT's solution :) Thanks chatGPT
def addTwoNumbers(l1, l2):
        # dummy, the head or starting point
        dummy = ListNode(0)
        # unline dummy, current will change through loop
        current = dummy
        # eg. 9 + 3 = 2, carry = 1
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            # take only 1 int, the surpassed value will be passed with 'carry'
            # also set the same value dummy.next in 1st time, as current&dummy points the same node 
            carry = total // 10
            current.next = ListNode(total % 10)
            # move on to next nodes (current,l1,l2)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # create new node if carry exceeds
        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next
    
# Example usage:
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

start_time = time()
result = addTwoNumbers(l1, l2)
end_time = time()

while result:
    print(result.val, end=" ")
    result = result.next

print("elapsed:",end_time - start_time)