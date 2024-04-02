from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        graph = self.build(prerequisites)
        print(graph)
        return True
    def build(self,edges): # [1,0] 0 -> 1 
        d = defaultdict(int)
        for pointed,base in edges:
            if not d[base]:
                d[base] = []
            if not d[pointed]:
                d[pointed] = []
            d[base].append(pointed)
        
        return d

x =[[1,0],[0,1]]
print(Solution().canFinish(2,x))