# Create a program that swaps the values of two variables.

print("                                             ")
variableOne = input("Type your first random variable: ")
variableTwo = input("Type your second random variable: ")

print("                                             ")
print("These are your random variables BEFORE swapping")
print("First random variable: ", variableOne)
print("Second random variable: ", variableTwo)



# Swappin'

temporaryHolder = variableOne
variableOne = variableTwo
variableTwo = temporaryHolder

print("                                             ")
print("These are your random variables AFTER swapping")
print("First random variable: ", variableOne)
print("Second random variable: ", variableTwo)
print("                                             ")
