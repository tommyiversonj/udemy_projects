# immutable in is a fundamental concept in Python, meaning that once an object is created, it cannot be modified.
# Immutable data types include integers, floats, strings, and tuples.
# Immutable data types are useful when you need to ensure that the content of a data structure cannot be changed.
# Immutable data types are also useful when you need to create a new object with the same content
# but a different identity, such as when you need to create a new string with the same content as an existing string.
# Immutable data types are also useful when you need to create a new object with the same content

X = 10 
print("original value of X:", X, type(X))  # Prints the original value and type of X
print("ID of X:", id(X))  # Prints the ID of X

x2 = X + 5 # Creates a new integer object with the value of X + 5
print("Modified X:", x2) # Prints the modified value of X
print("ID of modified X:", id(x2))  # Prints the ID of the modified X

