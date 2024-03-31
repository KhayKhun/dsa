my_graph = {
    'a' : ['c','b'],
    'b' : ['d'],
    'c' : ['e'],
    'e' : [],
    'f' : [],
    'd' : ['f'],
}
my_graph2 = {
    'f' : ['g','i'],
    'g' : ['h'],
    'h' : [],
    'i' : ['g','k'],
    'j' : ['i'],
    'k' : [],
}

undirected_graph = [
    ['i','j'],
    ['i','k'],
    ['m','k'],
    ['l','k'],
    ['o','n'],
]

def build_graph(edges):
    graph = {}
    for i,j in edges:
        if not i in graph: graph[i] = []
        if not j in graph: graph[j] = []
        graph[i].append(j)
        graph[j].append(i)
    return graph


# print(build_graph(undirected_graph))

def depth_first_values(graph,point):
    stack = [point]
    values = []
    while len(stack) > 0:
        current = stack.pop()
        values.append(current)

        for i in graph[current]:
            stack.append(i)

    return values

def depth_first_values_recursive(graph,point):
    arr = [point]
    for i in graph[point]:
        arr += depth_first_values_recursive(graph,i)

    return arr

def breadth_first_values(graph,point):
    queue = [point]
    values = []
    while len(queue) > 0:
        current = queue[0]
        values.append(current)
        queue.remove(current)

        neighbors = graph[current]
        for i in neighbors:
            queue.append(i)
    return values

# 0(e), edges || O(n^2


def hasPath(graph,src,dst):
    stack = [src]
    already = set()
    while len(stack) > 0:
        current = stack.pop()
        already.add(current)
        for i in graph[current]:
            if i == dst:
                return True
            if not i in already: stack.append(i)
        
    return False

def hasPathRecursive(graph,src,dst):
    if src == dst:return True

    for i in graph[src]:
        if hasPathRecursive(graph,i,dst): return True
        
    return False

# print(depth_first_values(my_graph,'a'))
# print(depth_first_values_recursive(my_graph,'a'))
# print(hasPathRecursive(my_graph2,'j','k'))
# print(hasPath(build_graph(undirected_graph),'i','m'))
