# Challenge: Write a program to print the multiplication table of a given number.

# PROCESS ON SOLVING CODING CHALLENGES

# 1. Understand the Problem
# Inputs: integer
# Outputs: multiplication table of a given number
# Restrictions:

# 2. Examples

# Example 1:
# Input :  5
# Output : 5 * 1 = 5
#          5 * 2 = 10
#          5 * 3 = 15
#          5 * 4 = 20
#          5 * 5 = 25
#          5 * 6 = 30
#          5 * 7 = 35
#          5 * 8 = 40
#          5 * 9 = 45
#          5 * 10 = 50

# Example 2:
# Input :  8
# Output : 8 * 1 = 8
#          8 * 2 = 16
#          8 * 3 = 24
#          8 * 4 = 32
#          8 * 5 = 40
#          8 * 6 = 48
#          8 * 7 = 56
#          8 * 8 = 64
#          8 * 9 = 72
#          8 * 10 = 80
#          8 * 11 = 88
#          8 * 12 = 96

# 3. Pseudocode

# make a bucket to put the given number
# Bonus: make a bucket to store the requested maximum multiplicand number
# Sample: In 7*9 according to the horizontal method of multiplication:
# 7 is the multiplier or given number (the leftmost number)
# 9 is the multiplicand
# use for loop and i in range to recreate i++ logic, to count from 0 to the maximum_number_of_multiplicationTable
# define another variable to store the result of the multiplication for one iteration
# use print() function to create the multiplication table

# 4. Solve/Simplify

given_number = int(input("Type a given number: "))
maximum_multiplicandNumber = int(input("Type the maximum multiplicand number of the multiplication table: "))

for i in range(maximum_multiplicandNumber):
    result = given_number * i
    print(f"{given_number} * {i} = {result}")




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

# Test 1
# Type a given number: 1
# Type the maximum number of the multiplication table: 2
# 1 * 0 = 0
# 1 * 1 = 1

# Test 2
# Type a given number: 7
# Type the maximum multiplicand number of the multiplication table: 51
# 7 * 0 = 0
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# 7 * 4 = 28
# 7 * 5 = 35
# 7 * 6 = 42
# 7 * 7 = 49
# 7 * 8 = 56
# 7 * 9 = 63
# 7 * 10 = 70
# 7 * 11 = 77
# 7 * 12 = 84
# 7 * 13 = 91
# 7 * 14 = 98
# 7 * 15 = 105
# 7 * 16 = 112
# 7 * 17 = 119
# 7 * 18 = 126
# 7 * 19 = 133
# 7 * 20 = 140
# 7 * 21 = 147
# 7 * 22 = 154
# 7 * 23 = 161
# 7 * 24 = 168
# 7 * 25 = 175
# 7 * 26 = 182
# 7 * 27 = 189
# 7 * 28 = 196
# 7 * 29 = 203
# 7 * 30 = 210
# 7 * 31 = 217
# 7 * 32 = 224
# 7 * 33 = 231
# 7 * 34 = 238
# 7 * 35 = 245
# 7 * 36 = 252
# 7 * 37 = 259
# 7 * 38 = 266
# 7 * 39 = 273
# 7 * 40 = 280
# 7 * 41 = 287
# 7 * 42 = 294
# 7 * 43 = 301
# 7 * 44 = 308
# 7 * 45 = 315
# 7 * 46 = 322
# 7 * 47 = 329
# 7 * 48 = 336
# 7 * 49 = 343
# 7 * 50 = 350

# Test 3
# Type a given number: 3
# Type the maximum number of the multiplication table: 100
# 3 * 0 = 0
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
# 3 * 7 = 21
# 3 * 8 = 24
# 3 * 9 = 27
# 3 * 10 = 30
# 3 * 11 = 33

# Error 1: input not converted using int()
# for i in range(maximum_number_of_multiplicationTable):
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: 'str' object cannot be interpreted as an integer

