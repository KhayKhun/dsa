from random import shuffle

def bogoSort(list):
    attempts = 0
    while isSorted(list) == False:
        attempts += 1
        shuffle(list)
    
    return (attempts,list)
    
    
def isSorted(list):
    for i in range(0, len(list)-1):
        if list[i] > list[i+1]:
            return False
        
    return True
        
l = [4,3,2,1,99,54]
print(bogoSort(l))