# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
b = 0

while 1: # Creates infinite loop, breaks in some conditions.
    x = input("Do your transaction: ")
    if not x:
        break
    n = x.split(" ")
    mode = n[0]
    value = int(n[1])
    if mode == "D":
        b += value
    elif mode == "W":
        b -= value
    else:
        pass

print(b)