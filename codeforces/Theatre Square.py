n,m,a = map(int, input().split())

an = n // a if a < n else 1
if a < n and n % a != 0: an += 1

am = m // a if a < m else 1
if a < m and m % a != 0: am += 1

print(an * am)