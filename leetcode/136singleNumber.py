def singleNumber(nums):
        result = 0
        for num in nums:
            result ^= num #XOR returns true(1) only when input differs
        return result

# Example usage
nums1 = [2,2,1,3,4,5,5,4,3]

print(singleNumber(nums1))  