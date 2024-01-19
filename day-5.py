# Challenge: Write a program to find the maximum and minimum values in a list.

# PROCESS ON SOLVING CODING CHALLENGES

# 1. Understand the Problem
# Inputs: list of values (integer or string)
# Outputs: minimum and maximum values
# Restrictions: Values can only be a list

# 2. Examples

# Example 1:
# Input: [0, 1, 2, 4, 5, 7, 8, 9, 100, 900]
# Output: The minimum value is: 0, The maximum value is: 900

# Example 2:
# Input: ["apple", "banana", "orange"]
# Output: The minimum value is: apple, The maximum value is: orange

# Example 3:
# Input: ["short", "qwerty", "longest"]
# Output: The minimum value is: longest, The maximum value is: short
# When using the min() and max() functions on a list of strings, values will be compared lexicographically (based on ASCII values)

# 3. Pseudocode

# Create a list variable and assign list with values
# Create a bucket to put the minimum value
# Use min() function to get the minimum value
# Print the value
# Create a bucket to put the maximum value
# Use max() function to get the maximum value
# Print the value

# 4. Solve/Simplify

# list1 = [0, 1, 2, 4, 5, 7, 8, 9, 100, 900]
# list1 = ["apple", "banana", "orange"]
# list1 = ["a", "qwerty", "longest"]
list1 = ["short", "qwerty", "longest"]

minimum_value = min(list1)
print(f"The minimum value is: {minimum_value}")

maximum_value = max(list1)
print(f"The maximum value is: {maximum_value}")



# 5. Refactor or Look Back



# 6. Test the code

# # Error1 python day-5.py 
# File "/workspaces/wwcode-python-2024/day-5.py", line 24
#     list1 = [0, 1, 2, 4, 5, 7, 8, 9, 100, 900, a, $, ^]
#                                                   ^
# SyntaxError: invalid syntax

# # Error2 python day-5.py 
#   File "/workspaces/wwcode-python-2024/day-5.py", line 24, in <module>
#     list1 = [0, 1, 2, 4, 5, 7, 8, 9, 100, 900, a, Z]
# NameError: name 'a' is not defined

# # Error3 python day-5.py 
#   File "/workspaces/wwcode-python-2024/day-5.py", line 26, in <module>
#     minimum_value = min(list1)
# TypeError: '<' not supported between instances of 'str' and 'int'



