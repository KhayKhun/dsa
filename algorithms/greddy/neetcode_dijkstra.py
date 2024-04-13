from typing import List,Dict
from collections import defaultdict
from heapq import heappop, heappush
# Accepted
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = self.build(edges)
        visited = set()
        costs = {node: float('inf') for node in range(n)} # 4 not here yet
        costs[src] = 0

        h = [(0,src)]
        while len(h):
            current_cost, current = heappop(h)
            if current in visited:
                continue
            visited.add(current)

            for key, val in graph[current]:
                if key in visited: continue

                total = current_cost + val
                if total < costs[key]:
                    costs[key] = total
                    heappush(h, (total,key))

        return {x: -1 if costs[x] == float('inf') else costs[x] for x in costs}
    
    def build(self, l):
        graph = defaultdict(list)
        for a,b,length in l:
            graph[a].append((b,length))
        return graph

# Input:
n = 7
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5],[5,6,1]]
src = 0

# Output:
# {{0:0}, {1:7}, {2:3}, {3:9}, {4:5}}

print(Solution().shortestPath(n,edges,src))
