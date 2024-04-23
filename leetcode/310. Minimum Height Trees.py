from collections import deque, defaultdict
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        edge_cnt = {}
        leaves = deque()

        for src, nei in adj.items():
            if len(nei) == 1:
                leaves.append(src)
            edge_cnt[src] = len(nei)

        while leaves:
            if n <= 2: return list(leaves)

            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)