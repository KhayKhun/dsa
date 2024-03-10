def intersection(nums1,nums2):
        both = set()
        res = set()
        for i in nums1:
            both.add(i)
        for i in nums2:
            if i in both:
                res.add(i)
        
        return list(res)
    
    
data = {
    'I' : 1,
'V '   :    5,
'X'     :   10,
'L'      :    50,
'C'       :    100,
'D'       :  500,
'M'        :   1000
}