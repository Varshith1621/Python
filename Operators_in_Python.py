# Assignment Operators
x = 5  # Assigns 5 to x
x += 3  # Equivalent to x = x + 3, now x is 8
x -= 2  # Equivalent to x = x - 2, now x is 6
x *= 4  # Equivalent to x = x * 4, now x is 24
x /= 6  # Equivalent to x = x / 6, now x is 4.0

# Comparison Operators
a = 10
b = 20
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)  # Output: False
print(a < b)  # Output: True
print(a >= 10)  # Output: True
print(b <= 25)  # Output: True

# Logical Operators
x = 5
y = 10
z = 15
# and operator
print(x > 0 and y > 5)  # Output: True (both conditions are True)
print(x > 10 and z > 10)  # Output: False (one of the conditions is False)
# or operator
print(x > 10 or z > 10)  # Output: True (one of the conditions is True)
print(x > 10 or y < 5)  # Output: False (both conditions are False)
# not operator
print(not(x > 10))  # Output: True (reverses False to True)
print(not(y < 5))  # Output: True (reverses False to True)

#  Bitwise Operators
a = 5  # In binary: 101
b = 3  # In binary: 011
# Bitwise AND
print(a & b)  # Output: 1 (binary: 001)
# Bitwise OR
print(a | b)  # Output: 7 (binary: 111)
# Bitwise XOR
print(a ^ b)  # Output: 6 (binary: 110)
# Bitwise NOT
print(~a)  # Output: -6 (inverts all bits)
# Left shift
print(a << 1)  # Output: 10 (binary: 1010)
# Right shift
print(a >> 1)  # Output: 2 (binary: 010)

# Arithmetic Operators (Already Covered in Chapter 2)
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a // b)  # Output: 3 (Floor Division)
print(a % b)  # Output: 1 (Modulus)
print(a ** b)  # Output: 1000 (Exponentiation)