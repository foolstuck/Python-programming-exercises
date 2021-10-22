# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple 
# which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

n = input("Please enter numbers, separate numbers with comma: ")

def num(n):
    l = n.split(",")
    t = tuple(l)
    print(l)
    print(t)

num(n)
