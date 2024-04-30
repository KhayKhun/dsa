n = int(input())

d = {}

for _ in range(n):
    s = input()

    if s not in d:
        d[s] = 0
        print('OK')
    else:
        d[s] += 1
        print(s + str(d[s]))
