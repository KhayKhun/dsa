from linkedList import LinkedList
from linkedList import LinkNode

l = LinkedList()
l.push(99)
l.push(3)
l.push(1)
l.push(6)
l.push(66)
l.push(0)
l.push(0)

def mergeSort(link):
    if link.size() <= 1:
        return link
    
    left_half, right_half = split(link)
    left = mergeSort(left_half)
    right = mergeSort(right_half)
    
    return merge(left, right)

def merge(leftLink,rightLink):
    both = LinkedList()
    currentL = leftLink.head
    currentR = rightLink.head
    
    while currentR and currentL:
        if currentL.val < currentR.val:
            both.push(currentL.val)
            currentL = currentL.next 
        else:
            both.push(currentR.val)
            currentR = currentR.next
            
    while currentR:
        both.push(currentR.val)
        
        currentR = currentR.next
    while currentL:
        both.push(currentL.val)
        currentL = currentL.next
    
    return both

def split(link):
    mid = link.size() // 2
    left = LinkedList()
    right = LinkedList()
    
    current = link.head
    count = 0
    
    while current:
        if count < mid:
            left.push(current.val)
            current = current.next
        else:
            right.push(current.val)
            current = current.next
        count += 1
        
    return left,right
            
    
print('input: ',l)
print('op: ',mergeSort(l))