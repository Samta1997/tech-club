def sum_of_digits(n):
    total_sum = 0  # Step 1: Initialize sum variable
    
    # Step 2: Loop until n becomes 0
    while n > 0:
        digit = n % 10  # Step 3: Extract the last digit
        total_sum += digit  # Step 4: Add the digit to the sum
        n = n // 10  # Step 5: Remove the last digit
        print(n)
    
    return total_sum  # Return the total sum

# Test the function
number = 12345
print(f'Sum of digits of {number} is {sum_of_digits(number)}')
