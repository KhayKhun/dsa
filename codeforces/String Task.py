s = list(input().lower())
res = ""

for i in s:
    if i in ['a','e','i','o','u','y']: continue

    res += '.'+i

print(res)