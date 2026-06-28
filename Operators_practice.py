# Logical Operator Practice
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Both numbers are greater than 10
print("Both numbers are greater than 10:", num1 > 10 and num2 > 10)
# At least one number is less than 5
print("At least one number is less than 5:", num1 < 5 or num2 < 5)
# First number is not greater than second
print("First number is not greater than second:", not (num1 > num2))

# Comparison Operator Challenge
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else if age < 18: 
    print("You are a minor")

# Membership Operator Exercise
text = input("Enter a string: ")
# Check if 'a' is in the string
print("Contains 'a':", 'a' in text)
# Check if "Python" is not in the string
print("Does not contain 'Python':", "Python" not in text)

# Bitwise Operator Task
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("a << 2 =", a << 2)
print("b >> 1 =", b >> 1)