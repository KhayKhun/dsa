def minimumBoxes(apple,capacity):
        capacity.sort() # 12345
        totalApple = sum(apple) #6
        totalBox = 0
        boxCapacity = 0
        i = len(capacity) - 1 #4
        while boxCapacity < totalApple: #0<6, 5<6
            boxCapacity += capacity[i] # 0+5
            totalBox += 1 #3
            i -= 1
            
        return totalBox
            
        
a = [1,3,2]
c = [4,3,1,5,2]

# print(minimumBoxes(a,c))

arr = [1,2,3,4,5]

for i in range(0,len(arr)):
    arr[i] = arr[i] +1
    
print(arr)
print(arr[1:])
