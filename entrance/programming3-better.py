n, m = map(int, input().split())
tb = [list(map(int, input().split())) for _ in range(n)] # n = number of input to store in tb
row_sums = [sum(row) for row in tb]
col_sums = []
for c in range(m):
    s = 0
    for r in range(n):
        s += tb[r][c]
    col_sums.append(s)

greatest = float('-inf')

for r in range(n):
    for c in range(m):
        greatest = max(greatest, row_sums[r] + col_sums[c] - tb[r][c])

print(greatest)
