n, m = map(int, input().split())
tb = [list(map(int, input().split())) for i in range(n)]

greatest = float('-inf')

for r in range(n):
    for c in range(m):
        sum_of_row = sum(tb[r])
        sum_of_col = 0
        for i in range(n):
            sum_of_col += tb[i][c]
        
        greatest = max(greatest, sum_of_row + sum_of_col - tb[r][c])
        
print(greatest)