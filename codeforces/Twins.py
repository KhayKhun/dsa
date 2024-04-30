n = int(input())

coins = sorted(list(map(int, input().split())), reverse=True)

m = sum(coins) / 2

current = 0
i = 0
while current <= m:
    current += coins[i]
    i += 1


print(i)