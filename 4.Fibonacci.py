def fibonacci(n):
    a, b = 0, 1  # Step 1: Initialize variables
    for _ in range(n):  # Step 2: Loop n times
        print(a, end=' ')  # Step 3: Print the current number
        next_number = a + b  # Step 4: Calculate the next number
        a = b  # Update current to previous
        b = next_number  # Update next to new current

# Call the function with desired n
fibonacci(5)  # This will print: 0 1 1 2 3
