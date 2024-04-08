class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return repr(self.val)

class BinarySearchTree:
    def __init__(self) -> None:
        self.head = None
    
    def has(self, v):
        if not self.head: return False
        stack = [self.head]
        while len(stack) > 0:
            c = stack.pop()
            if c.val == v: return True
            if c.left: stack.append(c.left)
            if c.right: stack.append(c.right)
        return False

    def size(self):
        if not self.head: return 0
        s = 0
        stack = [self.head]
        while len(stack) > 0:
            c = stack.pop()
            s += 1
            if c.left: stack.append(c.left)
            if c.right: stack.append(c.right)
        return s
    
    def height(self):
        if not self.head: return -1
        h = 0
        stack = [(self.head, 0)]
        while len(stack) > 0:
            node,index = stack.pop()
            h = max(h, index)
            if node.left: stack.append((node.left, index + 1))
            if node.right: stack.append((node.right,index + 1))
        return h

    def add(self, v, current = None):
        if not self.head: 
            self.head = Node(v)
            return
        if not current: current = self.head

        if v < current.val:
            if not current.left: current.left = Node(v)
            else: self.add(v,current.left)

        elif v > current.val:
            if not current.right: current.right = Node(v)
            else: self.add(v,current.right)

        elif v == current.val:
            if not current.right: current.right = Node(v)
            else:
                _r = current.right
                new_node = Node(v)
                current.right = new_node
                new_node.right = _r        

    def remove(self, v, node=None):
        if not self.head:
            return

        if node is None:
            node = self.head

        # Find the node to remove
        if v < node.val:
            node.left = self.remove(v, node.left)
        elif v > node.val:
            node.right = self.remove(v, node.right)
        else:
            # Node to remove found

            # Case 1: Node has no children or only one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 2: Node has two children
            # Find the minimum node in the right subtree
            min_node = node.right
            while min_node.left:
                min_node = min_node.left
            # Replace the current node's value with the value of the minimum node
            node.val = min_node.val
            # Remove the minimum node from the right subtree
            node.right = self.remove(min_node.val, node.right)

        return node

    def print_in_order(self, node):
        if not node: return []
        return self.print_in_order(node.left) + [node.val] + self.print_in_order(node.right)

    def __repr__(self) -> str:
        res = self.print_in_order(self.head)
        return repr(res)

# Example usage:
b = BinarySearchTree()
b.add(7)
b.add(3)
b.add(10)
b.add(6)
print(b)
print(b.size())
print(b.height())
print(b.has(3))
print(b.has(99))

# Removing a node
b.remove(7)
print(b,b.head)
