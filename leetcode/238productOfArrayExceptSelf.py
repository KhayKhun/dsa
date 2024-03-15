# time limit exceed #
class Solution:
    def productExceptSelf(self, nums):
        answer = []
        product = 1
        for i in nums:
            product *= i
            
        for i in nums:
            answer.append(int(product / i))

        return answer

sol = Solution()
n = [1,2,3,4]
# [24,12,8,6]
print(sol.productExceptSelf(n))