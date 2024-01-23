# Challenge: Write a program to count the occurrences of a specific character in a string.


# PROCESS ON SOLVING CODING CHALLENGES

# 1. Understand the Problem
# Inputs: string and specific character
# Outputs: integer
# Restrictions: 

# 2. Examples

# Example 1:
# Input: "hello" "e"
# Output: 1

# Example 2:
# Input: "door" "o"
# Output: 2

# 3. Pseudocode

# Define a function and name it countCharacterOccurence
# Create a parameter for the string and character inputs
# Create a variable for the counter to start at 0
# Find a way to iterate to each character in the string (for loop)
# Write the logic to "count the occurrences of a specific character in a string"
# If the all the character is looped use return statement to exit a function and return the count


# 4. Solve/Simplify

def countCharacterOccurence(string, character):

    # Error handling for empty string or invalid character
    if not string or len(character) != 1:
        raise ValueError("Invalid input. Please provide a non-empty string and a single character.")


    count = 0

    for everyChar in range(0, len(string)):
        if character in string[everyChar]:
            count = count + 1

    return count


# 5. Refactor or Look Back

# - Time Complexity
# - Space Complexity (Memory Usage)
# - Code Readability and Maintainability
# - Error Handling
# - Optimizations
# - Testing: unit testing and pytest
# - Documentation: README file with instructions on how to use your code
# - Use version control systems like Git to track changes to your code and collaborate with others

# 6. Test the code

string = input("Type random word: ")
character = input("Which character shall I count?: ")
result = countCharacterOccurence(string, character)
print(f"The '{character}' occurs {result} in {string}")

# Additional test cases
print(countCharacterOccurence("hello", "e"))            # Output: 1
print(countCharacterOccurence("door", "o"))             # Output: 2
print(countCharacterOccurence("poppppppppp", "p"))      # Output: 10
print(countCharacterOccurence("hakuna matata", " "))    # Output: 2

# Optional: Document errors you encountered
# ERRORS

# 1. 
# print(countCharacterOccurence(hello, e))
# NameError: name 'hello' is not defined. Did you mean: 'help'?
#### I did not put the string argument inside quote

# 2. 
# return count
# NameError: name 'count' is not defined. Did you mean: 'counter'?

# 3
# print(countCharacterOccurence("hello", "e"))
# for everyChar in len(string):
# TypeError: 'int' object is not iterable
# Because I was trying to loop in the sum of the length of the string

# 4
# print(f"The {character}" occurs {counter} in {string}")                             
# SyntaxError: unterminated string literal (detected at line 47)
# I did not define these parameters outside the function

