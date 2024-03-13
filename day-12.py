# Challenge: Write a program to reverse a given string. If you want, take it a step further and use recursion.


given_string = input("Type a string you want to reverse: ")


def reverse_string(given_string):
    reversed_string = ""
    for char in given_string:
        reversed_string = char + reversed_string
    return reversed_string


result = reverse_string(given_string)
print(result)


# # Day 12

# Python Days of Code Challenge - Day 12 :jigsaw:
# :bulb: How It Works:
# :calendar: 60 Days, 60 Questions: Dive into daily Python challenges, each marking a step closer to coding mastery. You can start anytime in between as well!
# :handshake: Learning Together:
# Share your solutions, ask questions, and connect with fellow coders in this thread or on social media (Twitter, LinkedIn) - or Github!
# Don't forget to tag us @WWCodePython or use the hashtags #WomenWhoCodePython #PythonDaysofCode so we can celebrate your achievements!
# :gift: Bonus:
# React to today’s question with a ":question:" if you’d like us to solve this LIVE in our upcoming Python Code Jam Sessions.
# :brain: Today's Challenge:
# Write a program to reverse a given string.
# If you want, take it a step further and use recursion.
