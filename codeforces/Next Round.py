n, k = map(int, input().split())

scores = list(map(int, input().split()))

valid = scores[k - 1]

count = 0 
i = 0
while i < n and scores[i] > 0 and scores[i] >= valid:
    count += 1
    i += 1 


print(count)