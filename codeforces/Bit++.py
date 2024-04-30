t = int(input())

x = 0
for _ in range(t):
    x += 1 if '+' in input() else -1

print(x)
