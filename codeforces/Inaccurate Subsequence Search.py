from collections import defaultdict
t = int(input())
for _ in range(t):
    count = 0
    n, m, k = map(int,input().split())
    d, b_tb = defaultdict(int), defaultdict(int)

    a,b = input().split(), input().split()

    for i in b:
        b_tb[i] += 1

    for i in range(m-1):
        d[a[i]] += 1

    l = 0
    r = m - 1
    while r < n:
        d[a[r]] += 1
        match = 0
        for key,val in d.items():
            if key in b_tb and b_tb[key] != 0 and b_tb[key] <= val:
                match += 1
        if match >= k:
            count += 1
        
        r += 1
        d[a[l]] -= 1
        l += 1

    print(count)