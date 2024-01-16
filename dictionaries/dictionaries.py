#store value in key-value pairs

mydictionary = {
    "name": "ivan",
    "age": 23,
    "nationality": "Mexico"
}

#accessing a value in a dictonary
print(mydictionary["name"])
print(mydictionary.get("name"))

#acessing keys in dictonary
print(mydictionary.keys())

#accesing the values in a dictonary
print(mydictionary.values())

#update a dictonary value
mydictionary.update({"age":20})

#add a dictonary value
mydictionary["height"] = 170
print(mydictionary)

#remove an element from a dictonary
mydictionary.pop("height")

print(mydictionary)