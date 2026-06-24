# Common String Operations:
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: "John Doe"
greeting = "Hello! " * 3
print(greeting)  # Output: "Hello! Hello! Hello! "

""" String Methods:
upper(): Converts a string to uppercase.
lower(): Converts a string to lowercase.
strip(): Removes leading and trailing spaces from a string.
replace(old, new): Replaces a substring with another string. """
message = "  Hello, World!  "
print(message.strip())  # Output: "Hello, World!"
print(message.upper())  # Output: "HELLO, WORLD!"
print(message.lower())  # Output: "hello, world!"
print(message.replace("World", "Python"))  # Output: "Hello, Python!"

# Accessing String Characters:
text = "Python"
print(text[0])  # Output: P
print(text[2])  # Output: t
print(text[-1])  # Output: n
print(text[-3])  # Output: h

# Slicing Strings:
word = "Python Programming"
print(word[0:6])  # Output: Python (extracts from index 0 to 6)
print(word[:6])  # Output: Python (same as above)
print(word[7:18])  # Output: Programming (from index 7 to 18)