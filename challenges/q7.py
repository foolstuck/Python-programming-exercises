# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

input_str = input("Please enter 2d demensions: ")
dimensions = [int(x) for x in input_str.split(',')] # Separate input with comma and put values in a list.
rowNum = dimensions[0]
colNum = dimensions[1]
# Create 2D list with entered rows and cols, values are all 0 for now
multilist = [[0 for col in range(colNum)] for row in range(rowNum)] 

for row in range(rowNum): 
    for col in range(colNum):
        multilist[row][col] = row * col

print(multilist)