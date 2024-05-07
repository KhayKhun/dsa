from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(int)
        for n in nums: d[n] += 1

        res = [[] for _ in range(max(d.values()))]

        for key, val in d.items():
            for i in range(val):
                res[i].append(key)

        return res

