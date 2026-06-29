fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 3, True]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Accessing List Elements
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana

# Modifying List Elements
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']

'''Adding elements:
append(): Adds an element to the end of the list. '''
fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']
# insert(): Inserts an element at a specific index.
fruits.insert(1, "kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'orange', 'cherry']

'''Removing elements:
remove(): Removes the first occurrence of an element.'''
fruits.remove("orange")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry']
# pop(): Removes the element at a specific index (or the last item if no index is provided).
fruits.pop()  # Removes the last item
print(fruits)  # Output: ['apple', 'kiwi']
fruits.pop(0)  # Removes the first item
print(fruits)  # Output: ['kiwi']
# clear(): Removes all elements from the list.
fruits.clear()
print(fruits)  # Output: []