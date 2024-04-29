n = int(input())

solutions = [input().split() for _ in range(n)]
count = 0
for sol in solutions:
    c = 0
    for i in sol:
        if i == '1': c+=1
    if c >= 2: count += 1

print(count) 