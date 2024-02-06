# Challenge: Write a program to remove duplicates from a list.

# PROCESS ON SOLVING CODING CHALLENGES

# 1. Understand the Problem
# Inputs: list with duplicates
# Outputs: list: New list with duplicates removed
# Restrictions: Only list data type is the input

# 2. Examples

# Example 1:
# Input: test_list = [1, 2, 3, 4, 4, 5, 5, "banana", 5, "grape", "apple", "orange", 4, "banana", 5, "grape"]
# Output: test_list = [1, 2, 3, 4, 5, 'banana', 'apple', 'orange', 'grape']

# Example 2:
# Input: test_list = [1, 1, 1, 2, 3, 2, 3, "apple", "orange", 4, "banana", 5, "grape", "orange", 4, "banana"]
# Output: test_list = [1, 2, 3, 'apple', 4, 'banana', 5, 'orange', 'grape']

# 3. Pseudocode

# define a function with a parameter for the input list
# use set function to remove duplicates
# convert the set back to list and return that output

# 4. Solve/Simplify


# def duplicateRemover(given_list):
#     clean_list =  list(set(given_list))
#     return clean_list


# 5. Refactor or Look Back

def duplicateRemover(given_list):
    # Check if the input is a valid list
    if not isinstance(given_list, list):
        raise ValueError("Input must be a list")
    
    # Use a set to efficiently remove duplicates
    unique_set = set(given_list)

    # Preserve the order of elements by converting the set back to a list
    cleaned_list = list(unique_set)


    return cleaned_list

# - Time Complexity
# - Space Complexity (Memory Usage)
# - Code Readability and Maintainability
# - Error Handling
# - Optimizations
# - Testing: unit testing and pytest
# - Documentation: README file with instructions on how to use your code
# - Use version control systems like Git to track changes to your code and collaborate with others

# 6. Test the code

test_list1 = [1, 2, 3, 4, 4, 5, 5, "banana", 5, "grape", "apple", "orange", 4, "banana", 5, "grape"]
print(duplicateRemover(test_list1))

test_list = [1, 1, 1, 2, 3, 2, 3, "apple", "orange", 4, "banana", 5, "grape", "orange", 4, "banana"]
print(duplicateRemover(test_list))

not_list = 5
print(duplicateRemover(not_list))

not_list1 = "this is string"
print(duplicateRemover(not_list1))

# Error 1: I forgot to use print() to show the returned output
# zsh: command not found: 0

# Error 2: not_list -- test not list input
# print(duplicateRemover(not_list))
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^ 
#     line 39, in duplicateRemover
#     raise ValueError("Input must be a list")
# ValueError: Input must be a list

# Error 3: not_list1
# File "<stdin>", line 1
# SyntaxError: invalid syntax