
list = [[0, 2], [4, 6], [8, 10], [12, 14]]
list2 =  ["chair", "table", "desk", "vikas", "bed"]
# print(list[3])
# print(list[3][1])
# print(list2[0])
# print(list2[-5])
# print(list2.remove("chair"))
# print(list2)
# print(list2.insert(1,"Vikas"))
# print(list2)

# print(list2.sort())
# print(list2)

# print(list2.sort(reverse=True))
# print(list2)

x=list2.pop(3)          #extract from list
print(list2)



arctic_animals = ["penguin", "elephant", \
                    "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(2, "snowy owl")  
arctic_animals.sort()  
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())