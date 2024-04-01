# 1. build from [[int]] type to hash map type
# 2. get a list of each components
# 4. get the single(unpaired) edges, by: n - len(visited), >>count
# 5. check each components, if they are complete.
#     - by checking if the edge have connection with both of other edges
# 6. check only the between relation, if component have 2 edges

from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges):
        graph = self.build(edges)
        visited = set()
        components = []
        # get every components
        for i in graph:
            edges = self.get_all_edges_from_component(graph,i,visited)
            if edges: components.append(list(edges))

        count = n - len(visited) # also includ single edges (no pair)
        # check components
        for j in components:
            if self.check_is_complete(graph,j): count += 1

        return count

    def check_is_complete(self,graph,component): #list -> boolean
        if len(component) == 2: return component[1] in graph[component[0]] and component[0] in graph[component[1]]

        for i in component:
            for j in component:
                if not(i == j or j in graph[i]): return False

        return True

    def get_all_edges_from_component(self,graph,current,visited): # -> hash set 
        store= set()
        if current in visited: return False
        store.add(current)
        visited.add(current)
        stack = [current]

        while len(stack) > 0:
            x = stack.pop()
            for i in graph[x]:
                if not i in visited: 
                    b = self.get_all_edges_from_component(graph,i,visited)
                    store = store.union(b)
            
        return store

    def build(self,undirectedL): # -> hash map
        d = defaultdict(int)
        for a,b in undirectedL:
            if not a in d: d[a] = []
            if not b in d: d[b] = []
            d[b].append(a)
            d[a].append(b)
        
        return d
        