from typing import List
from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        graph, trusted_count = self.build(trust)
        if not len(trusted_count):
            return n if n == 1 else -1 # more than 1 ppl, noone trust each other? return -1
        for key,val in graph.items():
            if len(val) == 0 and trusted_count[key] == n-1: return key
        return -1
    
    def build(self,l):
        d = defaultdict(list)
        trusted_count = defaultdict(int)
        for i in l:
            d[i[0]].append(i[1])
            if not i[1] in d: d[i[1]] = []

        for i in l: 
            trusted_count[i[1]] += 1

        return d, trusted_count