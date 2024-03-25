#append methods adds an item to end of list
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

#extend method adds all element of a list to the end of the current list
fruits = ['apple', 'banana', 'cherry']
more_fruits = ['orange', 'grape', 'pear']
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'grape', 'pear']

#insert method inserts an element at specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']

#remove removes the first item from the list whose value matched
fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry', 'banana']

#pop- Removes the item at the given position in the list and returns it. If no index is specified, pop() removes and returns the last item in the list.
fruits = ['apple', 'banana', 'cherry']
fruit = fruits.pop()
print(fruit)  # Output: 'cherry'
print(fruits)  # Output: ['apple', 'banana']

#clear- Removes all items from the list
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)  # Output: []

#index- Returns the index of the first item whose value is equal to x
fruits = ['apple', 'banana', 'cherry']
index = fruits.index('banana')
print(index)  # Output: 1

#count- Returns the no of time an element appears in the list
fruits = ['apple', 'banana', 'cherry', 'banana']
count = fruits.count('banana')
print(count)  # Output: 2

#sort-Sorts the list in ascending order
fruits = ['banana', 'apple', 'cherry']
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry']

#sort(reverse=true) - Sort the list in descending order
fruits = ['banana', 'apple', 'cherry']
fruits.sort(reverse=True)
print(fruits)  # Output: ['cherry', 'banana', 'apple']

#reverse() - Reverses the elements of the list in place.
fruits = ['banana', 'apple', 'cherry']
fruits.reverse()
print(fruits)  # Output: ['cherry', 'apple', 'banana']

#copy() - Returns a shallow copy of the list.
fruits = ['apple', 'banana', 'cherry']
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: ['apple', 'banana', 'cherry']

#slicing a list- Is used to slice a list and return a new list
fruits = ['apple', 'banana', 'cherry']
newFruits = fruits[0:1]
print(newFruits) # Output: ['apple']


