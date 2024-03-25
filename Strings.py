#Capitalize method
str = "hello world"
capitalized_str = str.capitalize()
print(capitalized_str)  # Output: Hello world

#Upper method
str = "hello world"
upper_str = str.upper()
print(upper_str)  # Output: HELLO WORLD

#Lower method
str = "HELLO WORLD"
lower_str = str.lower()
print(lower_str)  # Output: hello world

#Title method
str = "hello world"
title_str = str.title()
print(title_str)  # Output: Hello World

#strip method
str = "   hello world   "
stripped_str = str.strip()
print(stripped_str)  # Output: hello world

#replace method
str = "hello world"
replaced_str = str.replace("world", "Python")
print(replaced_str)  # Output: hello Python

#split method
str = "hello,world,python"
split_str = str.split(",")
print(split_str)  # Output: ['hello', 'world', 'python']

#join method
list = ['hello', 'world', 'python']
joined_str = ",".join(list)
print(joined_str)  # Output: hello,world,python

#startsWith method
str = "hello world"
starts_with_hello = str.startswith("hello")
print(starts_with_hello)  # Output: True

#endsWith method
str = "hello world"
ends_with_world = str.endswith("world")
print(ends_with_world)  # Output: True

#find method
str = "hello world"
index_of_world = str.find("world")
print(index_of_world)  # Output: 6

#length of String
string = "Hello World"
length = len(string)
print(length)  # Output: 11

#Slicing the string
string = "Hello World"
substring = string[3:8]  # Retrieves characters from index 3 to 7 (inclusive start, exclusive end)
print(substring)  # Output: "lo Wo"

string = "Hello World"
substring = string[-5:-2]  # Retrieves characters from the 5th character from the end to the 2nd character from the end
print(substring)  # Output: "Wor"

string = "Hello World"
substring = string[:5]  # Retrieves characters from the beginning to index 4 (exclusive end)
print(substring)  # Output: "Hello"

substring = string[6:]  # Retrieves characters from index 6 to the end
print(substring)  # Output: "World"

#Reversing String
str = "hello world"
reversed_str = str[::-1]
print(reversed_str)  # Output: "dlrow olleh"














