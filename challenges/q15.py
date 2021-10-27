# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

x = input("Please enter a single digit number: ")

if len(x) != 1:
    print("You have entered invalid value.")
else:
    x = int(x)
    print(x + 11*x + 111*x + 1111*x)

