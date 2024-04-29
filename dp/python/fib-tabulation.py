n = int(input('Enter n-'))

tb = [0] * (n + 1)
tb[1] = 1

for i in range(1,n):
    tb[i + 1] += tb[i]
    if i < n - 1: tb[i + 2] += tb[i]

print(tb[n])