#1. Print every character in "Camus".
for x in "Camus":
    print(x)
#alt
print("Camus"[0]) #Print each of the indexed value.

#2. Takes 2 inputs and insert 2 values in a string and print.
obj = input("Please enter an objective.")
name = input("Please enter a name.")
str = "Yesterday I wrote a . I sent it to !"

def c5(obj, name):
    str = "Yesterday I wrote a " + obj + ". I sent it to " + name + "!"
    print(str)
c5(obj, name)

#2. Solution:
n = input("enter a string:")
m = input("enter another string:")
x = "Yesterday I wrote a {}. I sent it to {}!".format(n,m)
print(x) 

#3. Captalize a string.
me = "aldous Huxley was born in 1894."
me = me.capitalize()
print(me)

#4. "Where now? Who now? When now?". from str to a list.
w3 = "Where now? Who now? When now?"
w3 = w3.replace("When now?", "When now? ")
w3 = w3.split("? ")
w3.pop()
print(w3)
#5. Join a list into a string.
strList = ["The", "fox", "jumped", "over", "the", "fence", "."]
str = " ".join(strList)
str = str.replace(" .", ".")
print(str)
#6. Replace s with $.
x = "A screaming comes across the sky."
# Uses build-in replace method
print(x.replace('s', '$'))
# Uses a for loop, replace s with $ in each iteration
l = []
for i in x:
    if i == "s" or i == "S":
        i = "$"
        l.append(i)
    else:
        l.append(i)
print("".join(l))
#7. Find index of a letter.
x = "Animal"
print(x.index("n"))
#8. Slice the sentense, remove period.
x = "It was bright cold day in April, and the clocks were striking thirteen."

print(x[:-1])