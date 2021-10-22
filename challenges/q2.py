# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# CTRL+/ comment out selected area.

def fact(x):
    x = int(x)
    i = x
    while i != 0:
        x = x * (x - 1)
        i = i - 1
    return x

num = input("please enter an integer:")

print(fact(num))
# My failed answer

# Solution
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)    # recursive function

x = int(input()) # cast user input to integer

print(fact(x))