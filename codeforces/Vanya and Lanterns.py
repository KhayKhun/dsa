n,l = map(int, input().split())

lanterns = sorted(list(map(int, input().split())))

start = lanterns[0]
end = l - lanterns[-1]

gap = float('-inf')
for i in range(n - 1):
    gap = max(gap, (lanterns[i+1] - lanterns[i]) / 2)


print(max(start,end,gap))
