# Challenge: Write a function to count the number of vowels in a given string

# PROCESS ON SOLVING CODING CHALLENGES

# 1. Understand the Problem
# Inputs: string
# Outputs: integer
# Restrictions:
# - The input should be a string value
# - The output should be a numerical value, the total number of vowels in the given string


# 2. Examples

# Example 1:
# Input: "queue"
# Output: 4

# Example 2:
# Input: "sequoia"
# Output: 5


# 3. Pseudocode

# # Use a list to put all the uppercase and lowercase vowels
# vowels = ["a", "e", "i", "o", "u"]

# # Define the function and name it vowel_counter
# def vowel_counter(given_string):

# # convert the given string to lowercase
#     lowercase_string = given_string.lower()


# # create a variable to initialize count to 0
#     count = 0

# # iterate through each character in the lowercase string
#     for eachChar in lowercase_string:

#     # check if the character is a vowel
#         if eachChar in vowels:

#             # increase the count
#             count = count + 1

# # return the total count
#     return count


# 4. Solve/Simplify

vowels = ["a", "e", "i", "o", "u"]


def vowel_counter(given_string):
    lowercase_string = given_string.lower()

    count = 0
    for eachChar in lowercase_string:
        if eachChar in vowels:
            count = count + 1
    return count


# 5. Refactor or Look Back

# vowels = ["a", "e", "i", "o", "u"]

# def vowel_counter(given_string):
#     lowercase_string = given_string.lower()

#     count = 0
#     for eachChar in lowercase_string:
#         if eachChar in vowels:
#             count += 1
#     return count

# 6. Test the code

print(vowel_counter("queue"))   # Output: 4
print(vowel_counter("sequoia"))  # Output: 5
print(vowel_counter("12345"))  # Output: 0 (no vowels)


# # Day 3

# ```
# Python Days of Code Challenge - Day 3

# How It Works:
# - 60 Days, 60 Questions: Dive into daily Python challenges, each marking a step closer to coding mastery. You can start anytime in between as well!

# Learning Together:
# - [ ] Share your solutions, ask questions, and connect with fellow coders in this thread or on social media (Twitter, LinkedIn) - or Github!
# - [ ] Don't forget to tag us @WWCodePython or use the hashtags #WomenWhoCodePython #PythonDaysofCode so we can celebrate your achievements!

# Bonus:
# - [ ] React to today’s question if you’d like us to solve this LIVE in our upcoming Python Code Jam Sessions

# Today's Challenge:
# - [ ] Write a function to count the number of vowels in a given string
# ```

# ### Daily goals

# - [x] Code [Day 3](https://github.com/agcdtmr/wwcode-python-2024/blob/main/day-3.py)
# - [x] Write an awesome commit message and push your code!
# - [x] Continue writing on your documentation.
# - [x] Share your wins!
# - [x] Take care of yourself: pause, stretch, hydrate. More on [WWCode Code of Balance](https://www.womenwhocode.com/blog/category/mental-health).
