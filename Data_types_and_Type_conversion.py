# Data types in Python
name = "Varshith"  # String data type
age = 21 # Integer data type
height = 5.9  # Float data type
is_student = True  # Boolean data type

print(type(name))  # Output: <class 'str'>
print(type(age))  # Output: <class 'int'>   
print(type(height))  # Output: <class 'float'>
print(type(is_student))  # Output: <class 'bool'>

# Type conversion in Python
is_student = "Yes" # Changing the boolean value to a string
print(type(is_student))  # Output: <class 'str'>

age_float = float(age)  # Converting integer to float
print(age_float)  # Output: 21.0

V = "21" 
print(float(V)+age_float)  # Output: 42.0