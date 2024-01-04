#String methods 
string = "authentic77"

#slicing
print(string[2:5])  #the
print(string[:3])  #aut
print(string[2:])  #thentic77

#start to slice from end to the beginning
print(string[:-2]) #authentic

#upper case
print(string.upper()) #AUTHENTIC77

#lower case
print(string.lower()) #authentic77

#replace a string to another string
print(string.replace("authentic","false")) #false77

#split a string by a character
newstring = "my name is ivan"
print(newstring.split(" ")) #['my', 'name', 'is', 'ivan']

#string concantenation
print("hello" + "world")

#format strings
age = 23
text = "hello I am {} years old"
print(text.format(age))













