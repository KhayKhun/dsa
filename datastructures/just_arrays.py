from collections import defaultdict
def longest_subarray_size_k(nums,k):
    max_val = float('-inf')
    current = 0
    for i in range(len(nums)):
        current += nums[i]

        if i >= k-1:
           max_val = max(max_val,current)
           current -= nums[i-(k-1)] 
    return max_val

# smallest size of subarray, that the sum has >= target
def smallest_subarray(nums,target):
    current = 0
    smallest = float('inf') # store smallest size
    left = 0 # left index

    for right in range(len(nums)):
        current += nums[right]
        while current >= target:
            smallest = min(smallest, right - left + 1)
            current -= nums[left]
            left += 1

    return smallest

def longest_subarry_with_k_distint(l,k):
    d = defaultdict(int)
    left,right = 0, 0
    longest = float('-inf')

    while right < len(l):
        d[l[right]] += 1
        
        totalItem,size = 0,0
        for v in d.values(): 
            if v: totalItem += 1
            size += v  

        # rule violated
        if totalItem > k:
            d[l[left]] -= 1
            left += 1
        # if not, calculate the max values 
        else: longest = max(longest, size)
        right += 1

    return longest

arr = [4,2,1,7,8,1,2,8,1,0]
l = ["A","C","A","H","I","I","B","P"]

# print(longest_subarray_size_k(arr,3))
# print(smallest_subarray(arr,8))
print(longest_subarry_with_k_distint(l,2))