a,b = map(int, input().split())

_a = int(a)
_b = int(b)

while b != 0:
    a,b = b, a%b

lcm = (_a * _b) // a

print('gcd: ',_a)
print('lcm: ',lcm)