# Knapsack Problem
# bag contains size and value
# find the maximum value we can carry by not exceeding the capicity
# return the max val 
from typing import List

def best_value_in_capacity(bag: List[List[int]], max_capacity: int) -> float:
    for item in bag: item.append(item[1] / item[0]) # append size/value ratio
    bag.sort(key=lambda x: x[2], reverse=True) # sort by ratio

    val = 0
    for item in bag:
        # can put whole 100% capacity of item
        if max_capacity >= item[0]:
            val += item[1]
            max_capacity -= item[0]
        # can't put 100%
        else:
            fraction = max_capacity / item[0]
            val += item[1] * fraction
            break  # capacity is fulled

    return val

bag = [
    # [size, value]
    [22, 19],
    [10, 9],
    [9, 9],
    [7, 6]
]

print(best_value_in_capacity(bag, 25))
