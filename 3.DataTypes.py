# Integer data type
# a = 10
# b = 5
# result = a + b
# print("Sum of integers:", result)


# Float data type
# x = 10.5
# y = 2.3
# result = x * y
# print("Multiplication of floats:", result)


#complex data types
# z = 5 + 7j
# print("Real part:", z.real)         
# print("Imaginary part:", z.imag)    


#List data type

'''1. Basic operation on list'''
# numbers = [10, 20, 30, 40, 50]

# # Access elements by index
# print("First element:", numbers[0])  # Output: 10
# print("Last element:", numbers[-1])  # Output: 50

# # Modify an element
# numbers[2] = 35
# print("Modified list:", numbers)  # Output: [10, 20, 35, 40, 50]

# # Add an element
# numbers.append(60)
# print("List after append:", numbers)  # Output: [10, 20, 35, 40, 50, 60]



'''2. List slicing'''
# # List slicing (getting sublists)
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# # Get elements from index 2 to 5 (exclusive)
# sublist = numbers[2:5]
# print("Sliced list:", sublist)  # Output: [30, 40, 50]

# # Slice with steps
# step_slice = numbers[1:7:2]
# print("List sliced with step:", step_slice)  # Output: [20, 40, 60]

# # Reverse a list using slicing
# reversed_list = numbers[::-1]
# print("Reversed list:", reversed_list)  # Output: [80, 70, 60, 50, 40, 30, 20, 10]



'''List Methods (Adding, Removing, and Counting Elements)'''
# # List methods: adding and removing elements
# fruits = ["apple", "banana", "cherry"]

# # Add elements
# fruits.append("orange")
# fruits.insert(1, "mango")  # Insert "mango" at index 1
# print("List after adding elements:", fruits)  # Output: ['apple', 'mango', 'banana', 'cherry', 'orange']

# # Remove elements
# fruits.remove("banana")  # Removes the first occurrence of "banana"
# popped_fruit = fruits.pop(2)  # Removes and returns the element at index 2
# print("Popped fruit:", popped_fruit)  # Output: "cherry"
# print("List after removing elements:", fruits)  # Output: ['apple', 'mango', 'orange']

# # Count the occurrences of an element
# count_mango = fruits.count("mango")
# print("Number of 'mango' in list:", count_mango)  # Output: 1


'''Sorting a List'''
# # Sorting a list
# numbers = [5, 3, 8, 1, 9, 2]

# # Sort in ascending order
# numbers.sort()
# print("Sorted list (ascending):", numbers)  # Output: [1, 2, 3, 5, 8, 9]

# # Sort in descending order
# numbers.sort(reverse=True)
# print("Sorted list (descending):", numbers)  # Output: [9, 8, 5, 3, 2, 1]


'''List Comprehensions'''
# # List comprehension to generate squares of numbers
# squares = [x**2 for x in range(1, 6)]
# print("List of squares:", squares)  # Output: [1, 4, 9, 16, 25]

# # List comprehension with condition
# even_numbers = [x for x in range(1, 11) if x % 2 == 0]
# print("Even numbers:", even_numbers)  # Output: [2, 4, 6, 8, 10]

'''Copying Lists'''
# Copying a list
# original = [1, 2, 3]
# copy_list = original.copy()  # Creates a shallow copy of the list
# copy_list.append(4)
# print("Original list:", original)  # Output: [1, 2, 3]
# print("Copied list:", copy_list)   # Output: [1, 2, 3, 4]


'''Nested Lists (Lists within Lists)'''
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Accessing elements in a nested list
# print("Element at row 1, column 2:", matrix[0][1])  # Output: 2
# print("Element at row 2, column 3:", matrix[1][2])  # Output: 6

# # Looping through a nested list
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()  # New line after each row


'''Combining Lists'''

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined = list1 + list2
# print("Combined list:", combined)  # Output: [1, 2, 3, 4, 5, 6]

# # Extending a list with another list
# list1.extend(list2)
# print("List after extending:", list1)  # Output: [1, 2, 3, 4, 5, 6]


''' Looping Through a List'''
# # Iterating through a list using a loop
# colors = ["red", "green", "blue"]

# # Using a for loop
# for color in colors:
#     print(color)

# # Using a while loop
# index = 0
# while index < len(colors):
#     print(colors[index])
#     index += 1


'''List of Mixed Data Types'''
# List with mixed data types
# mixed_list = [1, "apple", 3.14, True]

# for item in mixed_list:
#     print(f"Item: {item}, Type: {type(item)}")


'''List Length and Membership'''
# # Getting the length of a list
# fruits = ["apple", "banana", "cherry"]
# print("Length of the list:", len(fruits))  # Output: 3

# # Checking if an element exists in a list
# if "banana" in fruits:
#     print("Banana is in the list")
# else:
#     print("Banana is not in the list")


'''Clearing and Deleting a List'''
# # Clearing all elements from a list
# fruits = ["apple", "banana", "cherry"]
# fruits.clear()
# print("Cleared list:", fruits)  # Output: []

# # Deleting the entire list
# del fruits
# # print(fruits)  # This will raise an error because the list no longer exists
















