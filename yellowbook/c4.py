#1. Create a list of singers that you like.
singers = ["Jay Chou","Zhou Shen","Me Myself"]
#2. Create a tuple of the cities that you have traveled and their coordinates.
trips = []
zhengzhou = ("Zhengzhou","123,321")
toronto = ("Toronto","647,893")
new_york = ("New York","154,124")
trips.append(zhengzhou)
trips.append(toronto)
trips.append(new_york)
print(trips)
#3. Create a dictionary that introduces yourself.
me = {
    "name":"Mark",
    "age":"27",
    "height":"183cm",
    "nationality":"China",
    "color":"white",
    "author":"mr white"
}
print(me)
#4. Takes inputs of height, favorite color and author.
height = input()
color = input()
author = input()
me["height"] = height
me["color"] = color
me["author"] = author
print(me)
#5. Create a dictionary and add favorite singers.
favosinger = {}
favosinger["Jay Chou"] = "Seven Miles Perfume XD"
print(favosinger)
#6. When to use set in python
# A set is a collection which is unordered, unchangeable, and unindexed.
# Thus duplicated values are ignored. "Treated as one".
# Set can be used to remove duplicated values from a collection like a list.
