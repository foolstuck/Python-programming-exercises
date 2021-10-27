# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# num = input("Enter a number to check for even digit. Skip if you want to see 1000-3000: ")

# if num:
#     list = [int(x) for x in num]
#     for i in list:
#         if i % 2 != 0:
#             x = False
#             break
#         else:
#             x = True
#     if x:
#         print("It has all even digits!")
#     else:
#         print("It contains odd digits.")
# else:
#     t = True
#     printl = []
#     for i in range(1000,3001):
#         l = [x for x in str(i)]
#         for x in l:
#             if int(x) % 2 != 0:
#                 t = False
#         if t:
#             printl.append(l)
#     print(printl)
# Solution:
# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print(",".join(values))

# Stack Overflow
# create a list to append to
all_even = []
# ask for user input
num = input('Enter a number to check for even digit. Skip if you want to see 1000-3000: ')
# loop over either user input if they did input anything or over the range
# if they didn't input anything
for i in (num and [num]) or range(1000, 3000 + 1):
    # check if all digits in the number are even and
    # if they are append to the list
    if all(int(x) % 2 == 0 for x in str(i)):
        all_even.append(i)

# now check if user did input anything and if they did return the boolean
# of the list `all_even` which if the number had all even digits
# will contain one item so the bool will return True and or returns first True
# value or last one if none are True. So in case user did not input anything go to the
# next logical operator `or` and if there is anything in `all_even` print it out
# lastly print False if there were no values found at all
print(num and bool(all_even) or all_even or False)

