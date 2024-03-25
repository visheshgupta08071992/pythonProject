#Iterating list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Iterating Set
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)

#Iterating Dictionary using items
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)

#Iterating Dictionary using keys
person = {"name": "John", "age": 30, "city": "New York"}
for key in person.keys():
    print(key, ":", person[key])

#Iterating Dictionary using values
person = {"name": "John", "age": 30, "city": "New York"}
for value in person.values():
    print(value)