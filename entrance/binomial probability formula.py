def factorial(n):
    total = 1
    while n > 0:
        total *= n
        n-=1
    return total

def combinationSum(n,r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def round(number, n):
    factor = 10 ** n
    rounded_number = int(number * factor + 0.5) / factor
    return rounded_number

def binomialProbability(n, x, p):
    q = 1 - p
    nCx = combinationSum(n,x)

    return round(nCx * (p**x) * (q**(n-x)) * 100,2)

def binomialProbabilityRange(n, l, p):
    total = 0
    for i in l:
        total += binomialProbability(n,i,p)
    return total

students = 30
prob = 0.25

print(binomialProbability(students, 7, prob))
print(binomialProbabilityRange(students, [1,2,3,4], prob))

