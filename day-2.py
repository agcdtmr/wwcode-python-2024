# Challenge: Create a program to calculate the area of a circle given its radius.

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
