def addBinary(a: str, b: str) -> str:
        pos = -1
        carry = 0
        sum = ""
        
        while pos >= -max(len(a),len(b)):
            cur_a = a[pos] if -pos <= len(a) else "0"
            cur_b = b[pos] if -pos <= len(b)  else "0"
            
            base = (int(cur_a) + int(cur_b) + carry) % 2
            carry = (int(cur_a) + int(cur_b) + carry) // 2
                        
            sum = str(base) + sum
            pos -= 1
            
        if(carry): sum = "1" + sum
        
        return sum
    
a = "1010"
b = "1011"
print(addBinary(a,b))