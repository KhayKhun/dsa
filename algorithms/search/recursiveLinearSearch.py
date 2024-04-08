def recursiveLinearSearch(list,target):
    if len(list) == 0:
        return False
    
    if list[0] == target:
        return True
    else:
        print(list[1:])
        return recursiveLinearSearch(list[1:],target)

def verify(index):
    if index:
        print("Target found in list")
    else:
        print("Target not found in list")

input = [1,2,3,4,5,6,7]

output = recursiveLinearSearch(input, 10)
verify(output)