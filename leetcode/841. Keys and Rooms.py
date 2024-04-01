from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms):
        graph = self.build(rooms)
        visited = set()
        stack = [0]
        while len(stack) > 0:
            current = stack.pop()
            visited.add(current)

            for i in graph[current]:
                if not i in visited:
                    stack.append(i)

        return len(rooms) == len(visited)
    
    def build(self,edges):
        d = defaultdict(int)
        for i in range(len(edges)):
            d[i] = edges[i]
        return d
        