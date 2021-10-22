# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 
# between 2000 and 3200 (both included).

x = range(2000, 3200)
list = []
for i in x:
    if i % 7 == 0 and i % 5 != 0:
        list.append(i)
print(list)

# Solution

l = []
for i in range(2000, 3000):
    if i % 7 == 0 and i % 5 != 0:
        l.append(str(i))
print(','.join(l))


