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

