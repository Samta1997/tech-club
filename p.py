
# def sum_of_array(arr):
#     total=0
#     for item in arr:
#         if(item%2)==0:
#             total+=item
#     return total
# arr=[1,2,3,4,5,8,10]

# n=input()
# print(sum_of_array(arr))


# def count_vowels_consonants(input_string):
#     # Define vowels
#     vowels = "aeiouAEIOU"
    
#     # Initialize counters
#     vowel_count = 0
#     consonant_count = 0
    
#     # Iterate through each character in the input string
#     for char in input_string:
#         # Check if the character is an alphabet
#         if char.isalpha():
#             # Check if the character is a vowel
#             if char in vowels:
#                 vowel_count += 1
#             else:
#                 consonant_count += 1
    
#     return vowel_count, consonant_count

# # Example usage
# input_string = input("Enter a string: ")
# vowels, consonants = count_vowels_consonants(input_string)
# print(f"Number of vowels: {vowels}")
# print(f"Number of consonants: {consonants}")





# def find_maximum(arr):
#     # Check if the array is empty
#     if len(arr) == 0:
#         return None  # Return None if the array is empty
    
#     # Initialize the maximum with the first element of the array
#     max_num = arr[0]
    
#     # Iterate through the array to find the maximum number
#     for num in arr[1:]:
#         if num > max_num:
#             max_num = num
    
#     return max_num

# # Example usage
# arr = [10, 20, 45, 99, 36, 87, 12]
# maximum = find_maximum(arr)
# print(f"The maximum number in the array is: {maximum}")





# def fibonacci_sequence(n):
#     # Initialize the first two Fibonacci numbers
#     fib_sequence = [0, 1]
    
#     # Generate the Fibonacci sequence until it reaches the nth number
#     for i in range(2, n):
#         next_number = fib_sequence[i-1] + fib_sequence[i-2]
#         fib_sequence.append(next_number)
    
#     return fib_sequence[:n]

# # Example usage
# n = int(input("Enter the number of Fibonacci numbers to generate: "))
# fib_sequence = fibonacci_sequence(n)
# print(f"The first {n} numbers in the Fibonacci sequence are: {fib_sequence}")


# try:
#     x=1/0;
# except ZeroDivisionError:
#     print("print some error")





