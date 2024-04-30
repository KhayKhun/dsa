target = 'hello'
s = input()

i,j = 0,0

while j < len(s) and i < 5:
    if target[i] == s[j]:
        j += 1
        i += 1
    else:
        j += 1

res = 'YES' if i == 5 else 'NO'
print(res)