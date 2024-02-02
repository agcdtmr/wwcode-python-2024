# Challenge: Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.


# PROCESS ON SOLVING CODING CHALLENGES

# 1. Understand the Problem
# Inputs: string
# Outputs: integer
# Restrictions: 

# 2. Examples

# Example 1:
# Input: QWErty
# Output: uppercase: 3 and lowercase: 3

# Example 2:
# Input: LOWERCASE
# Output: uppercase: 9 and lowercase: 0

# 3. Pseudocode

# Define a function and assign a string as parameter 

# def letterCasesCalculator(str):

# # Reference: https://www.programiz.com/python-programming/methods/string/islower
# # Code a logic for calculates the number of uppercase and lowercase letters of the string argument

#     # Initialize counters for uppercase and lowercase letters
#     lowercase_str = 0
#     uppercase_str = 0

#     # Iterate through each character in the string
#     for everyElement in str:

#         # Check if the character is lowercase
#         if (everyElement.islower()):
#             lowercase_str += 1
#         # Check if the character is uppercase
#         else:
#             uppercase_str += 1

#     # Print the results
#     print(f"The number of lowercase characters is: ${lowercase_str}")
#     print(f"The number of uppercase characters is: ${uppercase_str}")


# 4. Solve/Simplify

# def letterCasesCalculator(str):
#     lowercase_str = 0
#     uppercase_str = 0
#     for everyElement in str:
#         if (everyElement.islower()):
#             lowercase_str += 1
#         else:
#             uppercase_str += 1
#     print(f"The number of lowercase characters is: ${lowercase_str}")
#     print(f"The number of uppercase characters is: ${uppercase_str}")

# 5. Refactor or Look Back

def letterCasesCalculator(str):
    lowercase_str = 0
    uppercase_str = 0
    for everyElement in str:
        if everyElement.islower():
            lowercase_str += 1
        elif everyElement.isupper():
            uppercase_str += 1
    print(f"The number of lowercase characters is: ${lowercase_str}")
    print(f"The number of uppercase characters is: ${uppercase_str}")

# - Time Complexity
# - Space Complexity (Memory Usage)
# - Code Readability and Maintainability
# - Error Handling
# - Optimizations
# - Testing: unit testing and pytest
# - Documentation: README file with instructions on how to use your code
# - Use version control systems like Git to track changes to your code and collaborate with others

# 6. Test the code

letterCasesCalculator("QWErty")  # Output: lowercase: 3 and uppercase: 3
letterCasesCalculator("LOWERCASE")  # Output: lowercase: 0 and uppercase: 9
letterCasesCalculator("uppercase")  # Output: lowercase: 9 and uppercase: 0
