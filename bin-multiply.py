def add_binary(x: str, y: str) -> str:
    if len(y) > len(x):
        x, y = y, x

    y = '0' * (len(x) - len(y)) + y

    result = ''
    carry = 0

    for i in range(len(x) - 1, -1, -1):
        bit_sum = int(x[i]) + int(y[i]) + carry
        result = str(bit_sum % 2) + result
        carry = 1 if bit_sum > 1 else 0

    if carry == 1:
        result = '1' + result

    return result


def multiply_single_bit(a, b):
    return int(a[0]) * int(b[0])

def multiply(x: str, y: str) -> int:
    n = max(len(x), len(y))
    x = x.zfill(n)
    y = y.zfill(n)
    
    if n == 0:
        return 0
    elif n == 1:
        return multiply_single_bit(x,y)
    
    first_half = n // 2  
    second_half = n - first_half  
    first_half_of_x = x[:first_half]  
    second_half_of_x = x[first_half:]  
    first_half_of_y = y[:first_half] 
    second_half_of_y = y[first_half:]  

    p1 = multiply(first_half_of_x, first_half_of_y)
    p2 = multiply(second_half_of_x, second_half_of_y)
    p3 = multiply(add_binary(first_half_of_x, second_half_of_x), add_binary(first_half_of_y, second_half_of_y))

    return (p1 << (2 * second_half)) + ((p3 - p1 - p2) << second_half) + p2


str1 = input()
str2 = input()

print(multiply(str1,str2))