my_set = {1, 2, 3}
print(my_set)

# Using the set() constructor to create a set
my_set2 = set([1, 2, 2, 3, 4])  # Duplicate values will be removed
print(my_set2)

#add - Adds a single element to the set.
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

#update(): Adds multiple elements to the set. You can pass a list, tuple, string, or another set as the argument.
my_set.update([7, 8, 9])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

#remove(): Removes a specific element from the set. Raises a KeyError if the element is not found.
my_set.remove(9)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

#discard(): Removes a specific element from the set. Does not raise an error if the element is not found.
my_set.discard(8)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

#pop(): Removes and returns an arbitrary element from the set. Since sets are unordered, you do not know which item that gets removed.
element = my_set.pop()
print(element)  # Output: Can be any element from the set
print(my_set)  # The set without the removed element

#clear(): Removes all elements from the set.
my_set.clear()
print(my_set)  # Output: set()

#union(): Returns a set that is the union of two sets.
A = {1, 2, 3}
B = {3, 4, 5}
C = A.union(B)
print(C)  # Output: {1, 2, 3, 4, 5}

#intersection(): Returns a set that is the intersection of two sets.
D = A.intersection(B)
print(D)  # Output: {3}