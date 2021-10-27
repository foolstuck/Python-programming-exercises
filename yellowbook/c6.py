#1. Print each letters in a list of strings.
x = ["whatever", "this is lame", "ok that's it"]

for i in x:
    for x in i:
        if x != ' ':
            print(x)

#2. Print numbers from 20 to 50
for x in range(20, 50+1):
    print(x)

#3. Print #1 and their index.
x = ["whatever", "this is lame", "ok that's it"]
n = 0
for i in x:
    print(i + " " + str(n))
    n += 1

#4. Infinite loop to guess a number.
a = 7
while True:
    x = input("Your guess? ")
    if x == 'q':
        break
    elif int(x) == 1:
        print("You are fucking smart.")
        break

#5. Multiply a list to another list
q = [8, 19, 148, 4]
p = [9, 1, 33, 83]
l = []

for x in q:
    for y in p:
        l.append(x * y)
print(l)