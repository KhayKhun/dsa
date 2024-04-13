def minRectangles(points, w):
    points.sort()
    current_end = float('-inf')
    rectangles = 0
    
    for x, y in points:
        if x > current_end:
            rectangles += 1
            current_end = x + w
        
    return rectangles

points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]]
print(minRectangles(points, 1))