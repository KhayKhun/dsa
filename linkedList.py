class Node:
    """
    An object for storing a single node
    """
    data = None
    next_node = None
    
    def __init__(self,data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    def size(self):
        """
        Takes linear time
        """
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        """
        Add new node at head of the list
        takes O(1) time
        """
        # assign the current head node as a next_node of the new new node
        new_node = Node(data)
        new_node.next_node = self.head
        # give head role to new node
        self.head = new_node
    
    def search(self,key):
        """
        Return first node matches the key
        Takes O(n) linear time
        """
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new node with the given data at the specified index position.
        Takes O(n) linear time.
        """
        if index == 0:  # If the index is 0, add the new node at the beginning
            self.add(data)
            
        elif index > 0:
            new_node = Node(data)
            position = index
            current = self.head

            # Iterate through the list until we reach the desired position or the end
            while position > 1 and current.next_node: # position = index. 
                current = current.next_node
                position -= 1

            # Insert the new node at the specified position
            new_node.next_node = current.next_node
            current.next_node = new_node
            
        else:
            raise IndexError("Index out of range")

    
    def remove(self,key):
        """
            Remove node containing data that matches key
            Takes O(n) time
        """
        current = self.head
        prev = None
        found = False
        
        while current and not found:
            # if head node is the desired node to be removed
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node # assign head to the next node
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node
                
        if not found:
            return None
        else:
            return current
    
    def __repr__(self):
        current = self.head
        nodes = []
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node:
                nodes.append("[%s]" % current.data)
            else:
                nodes.append("[Tail: %s]" % current.data)
                
            current = current.next_node
        
        return '-> '.join(nodes)
