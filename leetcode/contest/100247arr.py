def maximumHappinessSum(h,k):
        h.sort(reverse=True)
        total_happiness = 0

        for i in range(min(k, len(h))):
            total_happiness += max(0, h[i] - i)

        return total_happiness
    
print(maximumHappinessSum([12,1,42],3))