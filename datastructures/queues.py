class Node:
    next = None
    def __init__(self,v):
        self.val = v
    def __repr__(self) -> str:
        return "[Node %s]" % self.val

# pop
# push
# isEmpty

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        
    def isEmpty(self):
        return False if (self.first or self.last) else True    
    
    def push(self,v):
        newNode = Node(v)
        if self.isEmpty():
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        
    def pop(self):
        self.first = self.first.next
        
    def __repr__(self) -> str:
        current = self.first
        nodes = []
        while current:
            if current is self.first:
                nodes.append("[First: %s]" % current.val)
            elif current.next:
                nodes.append("[%s]" % current.val)
            else:
                nodes.append("[Last: %s]" % current.val)
                
            current = current.next
            
        return "->".join(nodes) if len(nodes) else "[]"
        
    
q = Queue()