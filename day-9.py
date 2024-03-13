# Challenge: Write a program to check if a number is even or odd.

# PROCESS ON SOLVING CODING CHALLENGES

# 1. Understand the Problem
# Inputs: number or integer
# Outputs: "The number is even or odd"
# Restrictions: the input should be an integer data type

# 2. Examples

# Example 1:
# Input: 7
# Output: odd

# Example 2:
# Input: 4
# Output: even

# 3. Pseudocode

# define a function
# code the logic of checking odd and even
# To determine whether a number is even or odd, it is divided by 2.
# If the remainder obtained after division is 0, then the number is referred to as an even number.
# On the other hand, when the remainder is not equal to zero, then the number is called an odd number.


# 4. Solve/Simplify

def checkNums(givenNum):
    if givenNum % 2 == 0:
        return f"{givenNum} is even"
    else:
        return f"{givenNum} is odd"


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
print(checkNums(3))  # 3 is odd
print(checkNums(0))  # 0 is even
print(checkNums(9))  # 9 is odd
print(checkNums(8))  # 8 is even


# Optional: Document errors you encountered

# 1 if givenNum % 2:
# {givenNum} is even
# {givenNum} is odd
# {givenNum} is even
# {givenNum} is odd

# 2
# if givenNum % 2 == 0:
#     return "{givenNum} is even"
# else:
#     return "{givenNum} is odd"
# Output:
# {givenNum} is even
# {givenNum} is odd
# {givenNum} is even
# {givenNum} is odd

# 7. Double Check the Documentation

# 8. Submit the Solution


# # Day 9

# Python Days of Code Challenge - Day 9 :jigsaw:
# :bulb: How It Works:
# :calendar: 60 Days, 60 Questions: Dive into daily Python challenges, each marking a step closer to coding mastery. You can start anytime in between as well!
# :handshake: Learning Together:
# Share your solutions, ask questions, and connect with fellow coders in this thread or on social media (Twitter, LinkedIn) - or Github!
# Don't forget to tag us @WWCodePython or use the hashtags #WomenWhoCodePython #PythonDaysofCode so we can celebrate your achievements!
# :gift: Bonus:
# React to today’s question with a ":question:" if you’d like us to solve this LIVE in our upcoming Python Code Jam Sessions.
# :brain: Today's Challenge:
# Write a program to check if a number is even or odd.
