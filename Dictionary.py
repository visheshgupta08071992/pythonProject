#Creates a new dictionary

new_dict = dict(name="rahul", hobby="playing")
print(new_dict)  # Output: {'name': 'rahul', 'hobby': 'playing'}

new_dict= {"name":"sachin","hobby":"sports"}
print(new_dict)  # Output: {'name': 'sachin', 'hobby': 'sports'}

#Retrieve value of a Key
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.get('name'))  # Output: Alice
print(my_dict.get('location', 'Unknown'))  # Output: Unknown
print(my_dict['age']) # Output: 25

#Retrieving key
my_dict = {'name': 'Alice', 'age': 25}
print(list(my_dict.keys()))  # Output: ['name', 'age']

#Retieving values
my_dict = {'name': 'Alice', 'age': 25}
print(list(my_dict.values()))  # Output: ['Alice', 25]

#Retrieving key value
my_dict = {'name': 'Alice', 'age': 25}
print(list(my_dict.items()))  # Output: [('name', 'Alice'), ('age', 25)]

#Add and update a key
my_dict = {'name': 'Alice', 'age': 25}
my_dict.update({'age': 26, 'location': 'New York'})
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'location': 'New York'}
my_dict["Country"]="USA"
my_dict["age"]=25
print(my_dict) # Output: {'name': 'Alice', 'age': 25, 'location': 'New York', 'Country': 'USA'}


#Pop a value
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.pop('age'))  # Output: 25
print(my_dict)  # Output: {'name': 'Alice'}

#Clear
my_dict = {'name': 'Alice', 'age': 25}
my_dict.clear()
print(my_dict)  # Output: {}

#copy
original = {'name': 'Alice', 'age': 25}
new_dict = original.copy()
print(new_dict)  # Output: {'name': 'Alice', 'age': 25}