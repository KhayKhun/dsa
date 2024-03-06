class Node:
    next = None
    prev = None
    def __init__(self,v):
        self.val = v
    def __repr__(self) -> str:
        return "[Node %s]" % self.val

# isEmpty
# pushToLeft
# pushToRight
# firstRight
# restRight
# firstLeft
# restLeft

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return False if (self.head or self.tail) else True
        
    def pushToLeft(self,v):
        newNode = Node(v)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def pushToRight(self,v):
        newNode = Node(v)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
         
    def firstLeft(self): return self.head
    def firstRight(self): return self.tail
        
    def restLeft(self):
        current = self.head.next if self.head else None
        nodes = []
        while current:
            if current.next:
                nodes.append("[%s]" % current.val)
            elif current is self.tail:
                nodes.append("[Tail: %s]" % current.val)                
                
            current = current.next
            
        return "->".join(nodes) if len(nodes) else "[]"
    
    def restRight(self):
        current = self.tail.prev if self.tail else None
        nodes = []
        while current:
            if current.prev:
                nodes.append("[%s]" % current.val)
            elif current is self.head:
                nodes.append("[Head: %s]" % current.val)  
                
            current = current.prev
            
        return "<-".join(nodes) if len(nodes) else "[]"
            
    def __repr__(self) -> str:
        current = self.head
        nodes = []
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.val)
            elif current.next:
                nodes.append("[%s]" % current.val)
            else:
                nodes.append("[Tail: %s]" % current.val)
                
            current = current.next
            
        return "->".join(nodes) if len(nodes) else "[]"
    
l = DoublyLinkedList()