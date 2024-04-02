treasure_map = [
    ['W','L','L','W','W'],
    ['W','L','L','W','L'],
    ['W','W','W','L','L'],
    ['W','W','L','L','W'],
    ['L','W','W','L','L'],
    ['L','L','W','W','W'],
]
def get_all_lands(grid,r,c,visited):
    rowInBounds = r >= 0 and r < len(grid)
    colInBounds = c >= 0 and c < len(grid[0])
    if not rowInBounds or not colInBounds: return False
    pos = (r,c)
    if pos in visited or grid[r][c] == 'W': return False

    visited.add(pos)

    get_all_lands(grid,r-1,c,visited)
    get_all_lands(grid,r+1,c,visited)
    get_all_lands(grid,r,c-1,visited)
    get_all_lands(grid,r,c+1,visited)

    return True

def land_count(grid):
    rows = len(grid)
    columns = len(grid[0])
    visited = set()
    land_count = 0

    for r in range(rows):
        for c in range(columns):
            if get_all_lands(grid,r,c,visited): land_count += 1

    return land_count


def explore_land_and_return_size(grid,r,c):
    stack = [(r,c)]
    size = 0

    while len(stack) > 0:
        row,col = stack.pop() # current row and col
        grid[row][col] = '#'
        size += 1

        if is_land(grid,row+1,col): stack.append((row+1,col))
        if is_land(grid,row-1,col): stack.append((row-1,col))
        if is_land(grid,row,col+1): stack.append((row,col+1))
        if is_land(grid,row,col-1): stack.append((row,col-1))

    return size

def is_land(grid,r,c):
    if r < 0 or r >= len(grid) or c < 0 or c>= len(grid[0]): return
    return grid[r][c] == 'L'

def minimum_land_size(grid):
    row_count = len(grid)
    col_count = len(grid[0])
    min_land = float('inf')

    for r in range(row_count):
        for c in range(col_count):
            if grid[r][c] == 'L':
                size = explore_land_and_return_size(grid,r,c)
                if size < min_land: min_land = size

    return min_land


print(minimum_land_size(treasure_map))