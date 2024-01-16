#A tuple is a collection which is ordered and unchangeable.
mytuple = ("apple", "banana","cherry")
print(mytuple)

"""
this syntax will give us an error
mytuple[1] = "strawberry"
"""

print(len(mytuple))

#unpacking a tuple

(first_value,second_value,third_value) = mytuple
print(first_value)

"""If the number of variables is less than the number 
of values, you can add an * to the variable name and the 
values will be assigned to the variable as a list: """

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

#joint two tuples
final_tuple = mytuple = fruits

#how many time an element is located in a tuple
print(final_tuple.count("apple"))

#which index in an element located
print(final_tuple.index("apple"))



