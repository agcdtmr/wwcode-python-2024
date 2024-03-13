# Challenge: Write a program to find the sum of all elements in a list.

# PROCESS ON SOLVING CODING CHALLENGES

# 1. Understand the Problem
# Inputs: list of integers
# Outputs: an integer, the sum of all elements in the list
# Restrictions:


# 2. Examples

# Example 1:
# Input: list1 = [3, 5, 7, 9, 11, 45]
# Output: 80

# Example 2:
# Input: list1 = [12, 15, 3, 10]
# Output: 40

# 3. Pseudocode

# Create a list and assign random numbers
# Find a way to iterate to each element in the list (for loop)
# Use add function to add each element in the list
# Define a bucket to put the total sum
# Print the sum


# 4. Solve/Simplify

sumTotal = 0

list1 = [3, 5, 7, 9, 11, 45]

for everyItem in range(0, len(list1)):
    sumTotal = sumTotal + list1[everyItem]

# 5. Refactor or Look Back


# Define the list
list1 = [3, 5, 7, 9, 11, 45]

# Use the sum function to find the sum of elements in the list
# Python provides a built-in sum function, which simplifies the process of finding the sum of elements in a list.
sum_total = sum(list1)


# 6. Test the code

print(f"The sum of all elements in the list is {sumTotal}")

print(f"The sum of all elements in the list is {sum_total}")

# # Day 4

# ```
# Python Days of Code Challenge - Day 4

# How It Works:
# - 60 Days, 60 Questions: Dive into daily Python challenges, each marking a step closer to coding mastery. You can start anytime in between as well!

# Learning Together:
# - [ ] Share your solutions, ask questions, and connect with fellow coders in this thread or on social media (Twitter, LinkedIn) - or Github!
# - [ ] Don't forget to tag us @WWCodePython or use the hashtags #WomenWhoCodePython #PythonDaysofCode so we can celebrate your achievements!

# Bonus:
# - [ ] React to today’s question if you’d like us to solve this LIVE in our upcoming Python Code Jam Sessions

# Today's Challenge:
# - [ ] Write a program to find the sum of all elements in a list.

# ```


# ### Daily goals

# - [x] Code [Day 4](https://github.com/agcdtmr/wwcode-python-2024/blob/main/day-4.py)
# - [x] Write an awesome commit message and push your code!
# - [x] Continue writing on your documentation.
# - [x] Share your wins!
# - [x] Take care of yourself: pause, stretch, hydrate. More on [WWCode Code of Balance](https://www.womenwhocode.com/blog/category/mental-health).
