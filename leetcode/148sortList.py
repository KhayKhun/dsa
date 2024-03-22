class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self) -> str:
        return '[%s]' %self.val
    
x = ListNode(400,ListNode(222))

# my solution (time limit exceeded 25/30)
class Solution:
    def sortList(self,head):    
        #start>> Get size
        listSize = self.size(head)
        if listSize <= 1:
            return head
        #end<<
        
        #start>> Get midpoint and split into left and right
        mid = listSize // 2
        dummyLeft = ListNode() #dummy left
        dummyRight = ListNode() #dummy left
        global_node = head
        i = 0
        while i < listSize and global_node:
            next_node = global_node.next
            if i < mid: self.push(dummyLeft,global_node.val)
            else: self.push(dummyRight,global_node.val)
            global_node = next_node
            i+=1 
        # result left and right
        left_half = self.sortList(dummyLeft.next)
        right_half = self.sortList(dummyRight.next)
        #end<<
        
        #start>> Merge
        i = 0
        j = 0
        leftSize = self.size(left_half)
        rightSize = self.size(right_half)
        resultDummyNode = ListNode()
        while i < leftSize and j < rightSize:
            if left_half.val < right_half.val:
                self.push(resultDummyNode, left_half.val)
                left_half = left_half.next
                i += 1
            else:
                self.push(resultDummyNode, right_half.val)
                right_half = right_half.next
                j += 1
        while i < leftSize:
            self.push(resultDummyNode, left_half.val)
            left_half = left_half.next
            i += 1
        while j < rightSize:
            self.push(resultDummyNode, right_half.val)
            right_half = right_half.next
            j += 1
            
        return resultDummyNode.next
        #end<<

    def push(self,head, val):
        current = head
        while current.next:
            current = current.next    
        current.next = ListNode(val)

    def size(self,head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size
    
        
s = Solution()
print(x,x.next)
res = s.sortList(x)
print(res,res.next)


# other's
def othersSortList(head):
  dummy = ListNode(0)
  dummy.next = head

  # Grab sublists of size 1, then 2, then 4, etc, until fully merged
  steps = 1
  while True:
    # Record the progress of the current pass into a single semi sorted list by updating
    # the next of the previous node (or the dummy on the first loop)
    prev = dummy

    # Keep track of how much is left to process on this pass of the list
    remaining = prev.next

    # While the current pass though the list has not been completed
    num_loops = 0
    while remaining:
      num_loops += 1

      # Split 2 sublists of steps length from the front
      sublists = [None, None]
      sublists_tail = [None, None]
      for i in range(2):
        sublists[i] = remaining
        substeps = steps
        while substeps and remaining:
          substeps -= 1
          sublists_tail[i] = remaining
          remaining = remaining.next
        # Ensure the subslist (if one was made) is terminated
        if sublists_tail[i]:
          sublists_tail[i].next = None

      # We have two sublists of (upto) length step that are sorted, merge them onto 
      # the end into a single list of (upto) step * 2
      while sublists[0] and sublists[1]:
        if sublists[0].val <= sublists[1].val:
          prev.next = sublists[0]
          sublists[0] = sublists[0].next
        else:
          prev.next = sublists[1]
          sublists[1] = sublists[1].next
        prev = prev.next
      
      # One list has been finished, attach what ever is left of the other to the end
      if sublists[0]:
        prev.next = sublists[0]
        prev = sublists_tail[0]
      else:
        prev.next = sublists[1]
        prev = sublists_tail[1]
    
    # Double the steps each go around
    steps *= 2

    # If the entire list was fully processed in a single loop, it means we've completely sorted the list and are done
    if 1 >= num_loops:
      return dummy.next