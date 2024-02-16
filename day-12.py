# Challenge: Write a program to reverse a given string. If you want, take it a step further and use recursion.


given_string = input("Type a string you want to reverse: ")


def reverse_string(given_string):
    reversed_string = ""
    for char in given_string:
        reversed_string = char + reversed_string
    return reversed_string


result = reverse_string(given_string)
print(result)
