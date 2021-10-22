#1. Take a int input, and return the square of the input.
x = input()
x = int(x) ** 2
print(x)

#2. Write a print function.
x = "random thing"
def printsomething(x):
    print(x)

printsomething(x)
#3. Function that takes 5 values in total, and 2 of them are optional
def five_value(a,b,c,d=0,e=0 ):
    print(1,2,3,d,e)

five_value(1,2,3)

#4. Funtion takes 2 integer parameters
def first(x):
    return x/2
def second(y):
    return y/4
x = first(60)
second(x)
print(second(x))

#5. Try and except
x = input()
def toFloat(x):
    try:
        x = float(x)
        return x
    except:
        return "not happening"

print(toFloat(x))