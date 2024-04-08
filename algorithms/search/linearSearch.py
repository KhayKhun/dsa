def linearSearch(list,target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i
        
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")

input = [1,2,3,4,5,6,7]

output = linearSearch(input, 40)
verify(output)