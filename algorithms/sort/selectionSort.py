def selectionSort(list):
    sorted = []
    while len(list) > 0:
        m = findMin(list)
        print(m)
        list.remove(m)
        sorted.append(m)
    return sorted  

def findMin(list):
    min = list[0]
    for i in range(1,len(list)):
        if list[i] < min:
            min = list[i]
    return min

l = []
print(selectionSort(l))