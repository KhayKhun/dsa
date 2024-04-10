import _heapq

data = [10,20,43,1,2,65,17,44,2,3,1]
_heapq.heapify(data)
print(data)

print(_heapq.heappop(data))
print(data)

# print(_heapq.heappush(data,0))
