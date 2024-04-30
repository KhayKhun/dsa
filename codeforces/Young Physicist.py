n = int(input())

x,y,z = 0,0,0
for _ in range(n):
    a,b,c = map(int, input().split())

    x += a
    y += b
    z += c

res = 'YES' if not (x or y or z) else 'NO'
print(res)
