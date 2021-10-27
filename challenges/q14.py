# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

input = input("Please write something: ")
up = 0
low = 0

for i in input:
    if i.islower():
        low += 1
    elif i.isupper():
        up += 1

print("Upper: " + str(up) + " Lower: " + str(low))