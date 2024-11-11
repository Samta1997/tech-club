def count_vowels_and_consonants(s):
    # Step 1: Initialize counters
    vowels_count = 0
    consonants_count = 0
    vowels = "aeiouAEIOU"  # String of vowels for checking

    # Step 2: Loop through each character
    for char in s:
        # Step 3: Check if the character is a letter
        if char.isalpha():  # Ignore non-alphabet characters
            if char in vowels:  # Check if it's a vowel
                vowels_count += 1  # Increment vowels counter
            else:  # It's a consonant
                consonants_count += 1  # Increment consonants counter

    # Step 5: Print the counts
    print(f'Vowels: {vowels_count}, Consonants: {consonants_count}')

# Test the function
test_str = "Hello World!"
count_vowels_and_consonants(test_str)
