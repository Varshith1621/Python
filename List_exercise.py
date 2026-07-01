# Create a list of 5 items
my_list = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Original List:", my_list)

# Add a new item to the end
my_list.append("Pineapple")
print("After adding to the end:", my_list)

# Add a new item at the second position (index 1)
my_list.insert(1, "Cherry")
print("After adding at second position:", my_list)

# Remove the third item (index 2)
removed_item = my_list.pop(2)
print("Removed Item:", removed_item)
print("After removing the third item:", my_list)




# Create a list of numbers
numbers = [45, 12, 78, 34, 23, 90, 11]

print("Original List:", numbers)

# Sort in descending order
numbers.sort(reverse=True)
print("Sorted in Descending Order:", numbers)

# Reverse the sorted list
numbers.reverse()
print("Reversed List:", numbers)