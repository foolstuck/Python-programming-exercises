# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class InputOutString(object):
    def __init__(self):
        self.s = ""
    def getString(self, msg):
        self.s = input(msg)
    def printString(self):
        print(self.s.upper())


strObj = InputOutString()
strObj.getString("Please enter a sentence: ")
strObj.printString()

