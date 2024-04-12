from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return '%s' % self.val

    def print_graph(self):
        def dfs(node, visited):
            if node is None:
                return

            print(node, [neighbor.val for neighbor in node.neighbors])
            visited.add(node.val)

            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    dfs(neighbor, visited)

        visited = set()
        dfs(self, visited)

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return
        visited = dict()

        def dfs(old):
            if old.val in visited: return visited[old.val]

            clone = Node(old.val)
            visited[old.val] = clone

            for n in old.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)

# Example usage:

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Define neighbors for each node
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

solution = Solution()
result = solution.cloneGraph(node1)

print("Original Graph:")
node1.print_graph()
print("---")
print("Cloned Graph:")
result.print_graph()
