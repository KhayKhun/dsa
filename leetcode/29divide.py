def divide(dividend: int, divisor: int) -> int:
        # Handle division by zero
        if divisor == 0:
            return 2**31 - 1
        
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Get the sign of the result
        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign = -sign
        if divisor < 0:
            divisor = -divisor
            sign = -sign
        
        # Find the largest multiple of the divisor that is less than or equal to the dividend
        multiple = 1
        while dividend >= (divisor << 1):
            divisor <<= 1
            multiple <<= 1
        
        # Perform division using binary search
        quotient = 0
        while multiple > 0:
            if dividend >= divisor:
                dividend -= divisor
                quotient += multiple
            divisor >>= 1
            multiple >>= 1
        
        # Apply the sign to the result
        return sign * quotient
            
print(divide(2147483647,2))