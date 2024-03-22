# get pivot
# divide into lessThan and greaterThan pivot lists

def quickSort(list):
    if len(list) <=0:
        return list
    
    pivot = list[0]
    
    lessThanP = []
    greaterThanP = []
    
    for x in list[1:]:
        if x < pivot:
            lessThanP.append(x)
        else:
            greaterThanP.append(x)
    
    return quickSort(lessThanP) + [pivot] + quickSort(greaterThanP)

# print(quickSort([4,6,7,8,1,0,0,45]))

a = [1,2,3,4]
print(a[1:-1])