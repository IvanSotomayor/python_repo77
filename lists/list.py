#LIST
# A list in python can store any type of data

my_list = [1,2,"ivan",'c',8.313,[1,2,3,2]]
print(my_list)

#Access list items
print(my_list[0])
print(my_list[-1])
print(my_list[0:4])

#check if an item exists in a list
thislist = ["apple", "banana", "cherry"]
print("apple" in thislist)

#change item value
thislist[1] = "randomFruit"
print(thislist)

#append list items
thislist.append("orange")

#insert items at a specific location
thislist.insert(1,"coco")

print(thislist)
