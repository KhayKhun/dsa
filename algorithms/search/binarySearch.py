def binarySearch(list,target):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        midpoint = (first + last) // 2
        
        if list[midpoint] == target:
            return midpoint
        elif target > list[midpoint]:
            first = midpoint + 1
        else:
            last = midpoint - 1
            
    return None
            
def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in lEist")

input = [1,2,3,4,5,6,7]

output = binarySearch(input, 4)
verify(output)