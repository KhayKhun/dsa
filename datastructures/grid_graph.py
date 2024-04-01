treasure_map = [
    ['W','L','W','W','W'],
    ['W','L','W','W','W'],
    ['W','W','W','L','W'],
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


print(land_count(treasure_map))