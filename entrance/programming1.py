a, b = map(int, input().split())
x = a // b
if a%b > 0: x += 1
print(x)