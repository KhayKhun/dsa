class LinkNode:
    next = None
    def __init__(self,v):
        self.val = v
    
    def __repr__(self):
        return "<Node: %s>" % self.val
    
# add
# clear
# size
# remove
# insert
# is exists
# is empty
# replace head
# replace rest
# last

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return False if self.head else True
    
    def add(self, v):
        newNode = LinkNode(v)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def clear(self):
        self.head = None
    
    def size(self):
        current = self.head
        len = 0
        while current:
            len += 1
            current = current.next
        
        return len
    
    def isExists(self,key):
        current = self.head        
        while current:
            if current.val == key:
                return True
            else:
                current = current.next
                
        return False
    
    def insert(self,v,index):
        current = self.head
        if index == 0 :
            self.add(v)
            return
        
        newNode = LinkNode(v)  
        for i in range(0,index-1):
            current = current.next
        
        if current:
            newNode.next = current.next if current.next else None
            current.next = newNode  
        else:
            self.add(v)        
    
    def remove(self,index):
        current = self.head
        if current and index == 0 : 
            self.head = current.next
            return
            
        for i in range(0,index-1):
            current = current.next
            
        if not current or not current.next:
            return
        
        current.next = current.next.next if current.next.next else None
    
    def replaceHead(self,v):
        if self.isEmpty(): return
        
        n = self.head.next
        self.head = LinkNode(v)
        self.head.next = n
        
    def replaceRest(self,arr):
        if self.isEmpty(): return
        if len(arr) == 0: self.head.next = None
        
        current = self.head
        for v in arr:
            newNode = LinkNode(v)
            current.next = newNode
            current = current.next
    
    def last(self, l):
        if self.isEmpty(): return None
        elif l and l.next:
            return self.last(l.next)
        else: return l
    
    def __repr__(self):
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