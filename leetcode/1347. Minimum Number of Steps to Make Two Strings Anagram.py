from collections import defaultdict
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d, res = defaultdict(int), 0

        for i in s: d[i] += 1
        for i in t: d[i] -= 1

        for i in d.values():
            if i > 0: res += i
        
        return res