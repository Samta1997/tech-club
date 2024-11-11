
# def is_palindrome(s):
#     s = s.lower()  # Normalize the string
#     return s == s[::-1]






# def is_palindrome(s):
#     s = s.lower()  # Normalize the string
#     left, right = 0, len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1

#     return True


# def is_palindrome(s):
#     s = s.lower()  # Normalize the string
#     # Base case: a single character or empty string is a palindrome
#     if len(s) <= 1:
#         return True
#     # Check first and last characters
#     if s[0] != s[-1]:
#         return False
#     # Recursively check the substring without the first and last characters

#     print(s[1:-1])
#     return is_palindrome(s[1:-1])


# is_palindrome("aabbaa")

