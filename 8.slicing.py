# Define a string to demonstrate slicing
s = "abcdefgh"

# Basic slicing - extracting characters from index 2 to 4 (5 is exclusive)
slice1 = s[2:5]  
print("s[2:5]:", slice1)

# Omitting start - extract from the beginning to index 3 (4 is exclusive)
slice2 = s[:4]  # 
print("s[:4]:", slice2)

# Omitting stop - extract from index 4 to the end
slice3 = s[4:]  #
print("s[4:]:", slice3)

# Using step - every 2nd character from index 1 to 6 (7 is exclusive)
slice4 = s[1:7:2]  # "bdf"
print("s[1:7:2]:", slice4)

# Extracting every second character from the whole string
slice5 = s[::2]  # "aceg"
print("s[::2]:", slice5)

# Negative indexing - extract characters from index -5 to -2 (-2 is exclusive)
slice6 = s[-5:-2]  # "def"
print("s[-5:-2]:", slice6)

# Reversing the string using slicing
reverse_slice = s[::-1]  # "hgfedcba"
print("s[::-1]:", reverse_slice)

# Using negative step to extract in reverse from index 5 to 3
slice7 = s[5:2:-1]  # "fed"
print("s[5:2:-1]:", slice7)

# Step of 3 - extract every third character from the entire string
slice8 = s[::3]  # "adg"
print("s[::3]:", slice8)

# Using out-of-range indices
# Even though 100 is out of range, it will slice until the end
slice9 = s[2:100]  # "cdefgh"
print("s[2:100]:", slice9)

# Out-of-range negative index
# -100 is far beyond the start, but Python will start from index 0
slice10 = s[-100:3]  # "abc"
print("s[-100:3]:", slice10)

# Trying slicing on a list
lst = [10, 20, 30, 40, 50, 60]

# Extract from index 1 to 3 (4 is exclusive)
list_slice1 = lst[1:4]  # [20, 30, 40]
print("lst[1:4]:", list_slice1)

# Reverse the list using slicing
list_reverse_slice = lst[::-1]  # [60, 50, 40, 30, 20, 10]
print("lst[::-1]:", list_reverse_slice)

# Extract every second element from the list
list_slice2 = lst[::2]  # [10, 30, 50]
print("lst[::2]:", list_slice2)

# Demonstrating string immutability and using slicing to modify a string
# Let's say we want to change the third character of the string to "Z"
new_string = s[:2] + "Z" + s[3:]
print('Modified string with "Z" at index 2:', new_string)

# Attempting to slice with a step of 0 will raise an error
try:
    error_slice = s[::0]
except ValueError as e:
    print("Error for s[::0]:", e)

# Example of an empty slice - start index is greater than stop index
empty_slice = s[5:2]  # Empty string
print("s[5:2]:", empty_slice)
