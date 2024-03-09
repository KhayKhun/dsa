def getCommon(nums1,nums2):
        same = 0
        i = 0
        j = 0

        while i < len(nums1) and  j < len(nums2):
            n1 = nums1[i]
            n2 = nums2[j]
            
            if n1 == n2:
                same = n1
                
                i+=1
                j+=1
                
            elif n1 > n2:
                j += 1
            
            elif n1 < n2:
                i += 1
            
        return same

nums1 = [1,2,3]
nums2 = [2,4]

print(getCommon(nums1, nums2))