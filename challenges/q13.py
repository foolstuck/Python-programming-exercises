# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

x = input("Please enter something: ")

letter_len = 0
num_len = 0

for x in x:
    if x.isalpha():
        letter_len = letter_len + 1
    elif x.isnumeric():
        num_len = num_len + 1

print("Letters: " + str(letter_len))
print("Digits: " + str(num_len))
