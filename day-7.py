# Challenge: Write a program to check if a number is positive, negative, or zero.

# PROCESS ON SOLVING CODING CHALLENGES

# 1. Understand the Problem
# Inputs: integer
# Outputs: print positive, negative, or zero.
# Restrictions:

# 2. Examples

# Example 1:
# Input: 0
# Output: zero

# Example 2:
# Input: -3
# Output: negative

# 3. Pseudocode

# if value has - in it then return negative,
# if value is 0 then return zero
# else return positive

# 4. Solve/Simplify

def numberChecker(intValue):

    # if not int or len(intValue) != 1:
    # raise ValueError("Invalid input. Please provide a number")

    if intValue == "0":
        return "zero"
    elif "-" in intValue:
        return "negative"
    else:
        return "positive"


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


test1 = numberChecker(input("Type a number: "))
print(f"The given number is {test1}")

print(numberChecker(str(-1)))
print(numberChecker(str(11)))
print(numberChecker(str(0)))
print(numberChecker(str(4)))
print(numberChecker(str(10000000)))
print(numberChecker(str(-10000000)))


# Optional: Document errors you encountered


# Error1
# I forgot that it's only str not string to convert
# print(string(numberChecker(-1)))
#           ^^^^^^
# NameError: name 'string' is not defined. Did you forget to import 'string'?

# Error2
#     print(numberChecker(11))
#           ^^^^^^^^^^^^^^^^^
#     if "-" in intValue:
#        ^^^^^^^^^^^^^^^
# TypeError: argument of type 'int' is not iterable

# Error3
# I cannot call the function inside a print function?
#     print(f"The number is typed is {numberChecker(test1)})
#           ^
# SyntaxError: unterminated f-string literal (detected at line 54)

# 7. Double Check the Documentation

# 8. Submit the Solution


# # Day 7

# ```
# Python Days of Code Challenge - Day 7

# How It Works:
# - 60 Days, 60 Questions: Dive into daily Python challenges, each marking a step closer to coding mastery. You can start anytime in between as well!

# Learning Together:
# - [ ] Share your solutions, ask questions, and connect with fellow coders in this thread or on social media (Twitter, LinkedIn) - or Github!
# - [ ] Don't forget to tag us @WWCodePython or use the hashtags #WomenWhoCodePython #PythonDaysofCode so we can celebrate your achievements!

# Bonus:
# - [ ]React to today’s question with a ":question:" if you’d like us to solve this LIVE in our upcoming Python Code Jam Sessions.

# Today's Challenge:
# - [ ] Write a program to check if a number is positive, negative, or zero.
# ```

# ### Daily goals

# - [x] Code [Day 7](https://github.com/agcdtmr/wwcode-python-2024/blob/main/day-7.py)
# - [x] Write an awesome commit message and push your code!
# - [x] Continue writing on your documentation.
# - [ ] Share your wins!
# - [x] Take care of yourself: pause, stretch, hydrate. More on [WWCode Code of Balance](https://www.womenwhocode.com/blog/category/mental-health).
