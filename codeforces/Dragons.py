s, n = map(int, input().split())

dragons = [tuple(map(int, input().split())) for _ in range(n)]
dragons.sort(reverse=True)

def check(s):
    while len(dragons) > 0:
        x, bonus = dragons.pop()

        if s > x:
            s += bonus
        else:
            return 'NO'
    
    return 'YES'

print(check(s))