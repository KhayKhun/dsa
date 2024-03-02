def recursiveBinarySearch(list,target):
    if len(list) == 0 :
        return False
    else:
        midpoint = (len(list)) // 2
        
        if list[midpoint] == target:
            return True
        else:
            if target > list[midpoint]:
                return recursiveBinarySearch(list[midpoint + 1:],target)
            else:
                return recursiveBinarySearch(list[:midpoint],target)
            
def verify(index):
    if index:
        print("Target found in list")
    else:
        print("Target not found in list")

input = [1,2,3,4,5,6,7]

output = recursiveBinarySearch(input, 10)
verify(output)