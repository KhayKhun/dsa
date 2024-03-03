# my solution (timed out error) :)
def threeSum(nums):
    print(nums)
    res = []
    
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                lst = [nums[i],nums[j],nums[k]]
                lst.sort() # this part so heavy
                if(nums[i]+nums[j]+nums[k] == 0 and lst not in res): 
                    res.append(lst)
    return res

# chat gpt
def threeSum(nums): 
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the input list
        
        res = []
        n = len(nums)
        
        for i in range(n):
            # Skip duplicate values for nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for nums[left] and nums[right]
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res

nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

print(threeSum(nums))