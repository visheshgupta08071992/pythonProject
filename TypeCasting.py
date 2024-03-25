# Implicit type conversion
x = 10       # integer
y = 5.5      # float

result = x + y   # x is implicitly converted to float
print(result)    # Output: 15.5


# Explicitly converting a float to an integer
x = 10.5
int_x = int(x)
print(int_x)  # Output: 10

# Explicitly converting an integer to a float
y = 5
float_y = float(y)
print(float_y)  # Output: 5.0

# Explicitly converting an integer to a string
z = 100
str_z = str(z)
print(str_z)  # Output: "100"

# Explicitly converting a tuple to a list
tuple_values = (1, 2, 3)
list_values = list(tuple_values)
print(list_values)  # Output: [1, 2, 3]

# Explicitly converting a list to a tuple
list_values = [4, 5, 6]
tuple_values = tuple(list_values)
print(tuple_values)  # Output: (4, 5, 6)

# Explicitly converting a list to a set
list_values = [1, 2, 2, 3, 3, 3]
set_values = set(list_values)
print(set_values)  # Output: {1, 2, 3}

# Explicitly converting an integer to a boolean
x = 10
bool_x = bool(x)
print(bool_x)  # Output: True
