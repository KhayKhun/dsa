grid = [ input().split() for _ in range(5) ]

for r in range(5):
    for c in range(5):
        if grid[r][c] == '1':
            diff_x = abs(r - 2)
            diff_y = abs(c - 2)

            print(diff_x + diff_y)
            break
