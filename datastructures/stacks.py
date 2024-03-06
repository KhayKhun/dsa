class Node:
    next = None
    def __init__(self,v):
        self.val = v
    def __repr__(self) -> str:
        return "[Node %s]" % self.val
    
# clear
# push
# top
# pop
# isEmpty

class Stack:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return False if self.head else True
    
    def clear(self):
        self.head = None
    
    def push(self, v):
        newNode = Node(v)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def top(self): return self.head
    
    def pop(self):
        self.head = self.head.next
    
    def __repr__(self) -> str:
        current = self.head
        nodes = []
        while current:
            nodes.append("%s" %current)
            current = current.next
        return "->".join(nodes) if len(nodes) else "[]"