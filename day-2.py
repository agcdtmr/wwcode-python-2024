# Challenge: Create a program to calculate the area of a circle given its radius.

# Notes
# The formula for calculating the area of a circle is given by:
# Area = pi ** radius
# Area = π ** radius
# Here:
# π (pi) is a mathematical constant approximately equal to 3.14159.
# radius means you square the length of the radius (multiply it by itself).
# So, in simpler terms, to find the area of a circle, you take the value of pi, multiply it by the square of the radius.

# PROCESS ON SOLVING CODING CHALLENGES

# 1. Understand the Problem
# Inputs:
# The input is the radius of the circle.

# Outputs:
# The output is the area of the circle.

# Restrictions:
# - The input should be a numerical value representing the radius.
# - The output should be a numerical value representing the area.

# 2. Examples

# Example 1:
# Input: 2
# Output: 12.566370614359172 (calculated area of a circle with a radius of 2)

# Example 2:
# Input: 4
# Output: 50.26548245743669 (calculated area of a circle with a radius of 4)


# 3. Pseudocode

# # What is the formula of finding the area of a circle
# # Area = pi ** radius
# # Area = π ** radius

# Create a pi variable and assign it to its value 3.14159
pi = 3.14159

# Use input to get the radius from the user from terminal
# input's value is string, convert it to integer
radius = int(input("What is the radius of the circle? "))

# Write the formula in a python way
area_of_circle = pi * radius ** 2

# print the result
print(area_of_circle)

# 4. Solve/Simplify

pi = 3.14159
radius = int(input("What is the radius of the circle? "))

area_of_circle = pi * radius ** 2
print(area_of_circle)


# 5. Refactor or Look Back

# def area_of_circle(radius):
#     if type(radius) not in [int, float]:
#         return "Invalid input. Please input integer or float type."

#     pi = 3.14159
#     areaOfCirle = pi * radius ** 2
#     return areaOfCirle

# 6. Code & Test

# Test with Valid Input
radius_valid = 5
area_valid = area_of_circle(radius_valid)
print(f"The area of a circle with radius {radius_valid} is {area_valid}")

# Test with Invalid Input
radius_invalid = "invalid"
area_invalid = area_of_circle(radius_invalid)
print(area_invalid)

# Test with Floating-Point Input
radius_float = 3.5
area_float = area_of_circle(radius_float)
print(f"The area of a circle with radius {radius_float} is {area_float}")

# Test with Negative Input
radius_negative = -6
area_negative = area_of_circle(radius_negative)
print(f"The area of a circle with radius {radius_negative} is {area_negative}")

# Test with Zero Input
radius_zero = 0
area_zero = area_of_circle(radius_zero)
print(f"The area of a circle with radius {radius_zero} is {area_zero}")

# Test with Large Input
radius_large = 1000
area_large = area_of_circle(radius_large)
print(f"The area of a circle with radius {radius_large} is {area_large}")

# # Day 2

# ```
# Python Days of Code Challenge - Day 2

# How It Works:
# - 60 Days, 60 Questions: Dive into daily Python challenges, each marking a step closer to coding mastery. You can start anytime in between as well!

# Learning Together:
# - [ ] Share your solutions, ask questions, and connect with fellow coders in this thread or on social media (Twitter, LinkedIn) - or Github!
# - [ ] Don't forget to tag us @WWCodePython or use the hashtags #WomenWhoCodePython #PythonDaysofCode so we can celebrate your achievements!

# Bonus:
# - [ ] React to today’s question if you’d like us to solve this LIVE in our upcoming Python Code Jam Sessions

# Today's Challenge:
# - [ ] Create a program to calculate the area of a circle given its radius.
# ```

# ### Daily goals

# - [x] Code [Day 2](https://github.com/agcdtmr/wwcode-python-2024/blob/main/day-2.py)
# - [x] Write an awesome commit message and push your code!
# - [x] Continue writing on your documentation.
# - [x] Share your wins!
# - [x] Take care of yourself: pause, stretch, hydrate. More on [WWCode Code of Balance](https://www.womenwhocode.com/blog/category/mental-health).
