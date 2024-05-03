length, a,b,c = map(int, input().split())
small = min(a,b,c)
memo = {}
def rec(size):
    if size in memo: return memo[size]
    if size == 0: return 1
    if size < 0 or size < small: return 0

    memo[size] = 1 + max(rec(size - a),rec(size - b),rec(size - c))
    return memo[size]


print(max(rec(length - a),rec(length - b),rec(length - c)))