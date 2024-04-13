import heapq
from typing import List

# TLE ;(
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        res = [float('inf')] * n
        res[0] = 0

        pq = [(0, 0)]  # (time, node)

        while pq:
            time, node = heapq.heappop(pq)
            if disappear[node] < time:
                continue
            for u, v, length in edges:
                if u == node:
                    neighbor = v
                elif v == node:
                    neighbor = u
                else:
                    continue
                if disappear[neighbor] > time + length and time + length < res[neighbor]:
                    res[neighbor] = time + length
                    heapq.heappush(pq, (time + length, neighbor))

        return [-1 if x == float('inf') else x for x in res]


# Test cases
solution = Solution()
print(solution.minimumTime(3, [[0,1,2],[1,2,1],[0,2,4]], [1,1,5]))  # Output: [0,-1,4]
print(solution.minimumTime(3, [[0,1,2],[1,2,1],[0,2,4]], [1,3,5]))  # Output: [0,2,3]
print(solution.minimumTime(2, [[0,1,1]], [1,1]))  # Output: [0,-1]
