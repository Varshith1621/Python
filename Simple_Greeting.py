# Simple Greeting Program

name = input("Enter your name: ")
age = input("Enter your age: ")

# Using + operator
print("Hello, " + name + "! You are " + age + " years old.")

# Using f-string
print(f"Hello, {name}! You are {age} years old.")





# String Manipulation Exercise
sentence = input("Enter a sentence: ")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Replaced:", sentence.replace("Varshith", "Abhinandhini"))
print("Stripped:", sentence.strip())





# Character Counter

text = input("Enter a string: ")

count = len(text.replace(" ", ""))

print("Number of characters (excluding spaces):", count)

# Escape Sequence Practice

print("Hello")
print("\tWorld")
print("This is a backslash: \\")