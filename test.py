def increase(s, index): 
    return s[:index] + str((int(s[index]) + 1) % 10 ) + s[index + 1:]
def decrease(s, index): 
    return s[:index] + str((int(s[index]) - 1 + 10) % 10 ) + s[index + 1:]


for i in range(1,4):
    print(i)
