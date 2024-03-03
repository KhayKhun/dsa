# my solution 1 (beats 23%)
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    string = ''.join(map(str, digits))
    added_int = int(string) + 1
    added_list = [int(i) for i in str(added_int)]
    return added_list

# my solution 2 (Beats 93.66% of users with Python)


def plusOne(digits):
    carry = 1
    index = len(digits) - 1
    while index > -1:
        sum = digits[index] + carry
        digits[index] = sum % 10
        carry = sum // 10
        index -= 1
    if carry:
        digits.insert(0, carry)
    return digits

# other solution


def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
    return [1] + digits

digits = [9, 9]
print(plusOne(digits))
