my_graph = {
    'a' : ['c','b'],
    'b' : ['d'],
    'c' : ['e'],
    'e' : [],
    'f' : [],
    'd' : ['f'],
}

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



print(depth_first_values(my_graph,'a'))
print(depth_first_values_recursive(my_graph,'a'))
