import heapq

def dijkstra(graph, start, end):
    visited = set()
    costs = {node: float('inf') for node in graph}
    pred = {node: [] for node in graph}
    costs[start] = 0
    min_heap = [(0, start)]
    
    while min_heap:
        current_cost, current = heapq.heappop(min_heap)
        if current == end:
            break
        if current in visited:
            continue
        visited.add(current)
        
        for key, val in graph[current].items(): # {'B':2}, {neighbour: cost}
            if key not in visited:
                total_cost = current_cost + val
                if total_cost < costs[key]:
                    costs[key] = total_cost
                    pred[key] = pred[current] + [current]
                    heapq.heappush(min_heap, (total_cost, key))
    
    return costs[end], pred[end] + [end]

graph = {
    'A': {'B':2, 'C':4},
    'B': {'A':2, 'C':3, 'D': 8},
    'C': {'A':4, 'B':3, 'D': 2, 'E':5},
    'D': {'B':8, 'C':2, 'E': 5, 'F':22},
    'E': {'C':5, 'F':1, 'D': 11},
    'F': {'D':22, 'C':1},
}

print(dijkstra(graph, 'A', 'F'))
